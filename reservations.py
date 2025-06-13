import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from edit_reservation import EditPage

class ReservationsPage(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.parent = parent
        self.db = db
        self.configure(bg='white')

        tk.Label(self, text='Your Reservations', fg='#3E23D6', font=('Inter', -32), bg='white').pack(pady=(20, 10))
                
        columns = [('Name', None), ('Flight Number', 100), ('Departure', 100), ('Destination', 100), ('Date', 100), ('Seat Number', 100)]
        
        self.table = Table(self,columns)
        self.insert_from_db()

        self.table.pack()

        btns = SubmitBtns(self)
        btns.create_btn('Edit', 'white', '#4492F7', 40, self.edit)
        btns.create_btn('Delete', 'white', '#EC2929', 40, self.delete)
        btns.create_btn('Go Back', 'white', "#000000", 40, self.goBack)
        btns.pack(pady=30)


    def insert_from_db(self):
        for entry in self.db.read_reservations():
            self.table.insert_entry(entry[0], entry[1:])

    def reset(self):
        self.table.delete_all()
        self.insert_from_db()            

    #btns
    def edit(self):
            id = self.table.return_selctedItem_ID()
            selected = self.table.return_selctedItem()
            if selected:
                editPage = EditPage(self, id, selected, self.db)
                editPage.grab_set()
                self.wait_window(editPage)
                self.reset()
            else:
                messagebox.showerror(message='Please select an entry first.') 

    def delete(self):
        sel = self.table.return_selctedItem()
        if sel:
            response = messagebox.askyesno(message='Are you sure you want to delete the selected entry?')      
            if response:
                self.db.delete_reservations(self.table.return_selctedItem_ID())
                self.table.delete_selected_item()
        else:
            messagebox.showerror(message='Please select an entry first.')

    def goBack(self):
        self.parent.change_frame('HomePage')
        
class Table(tk.Frame):
    def __init__(self, parent, columns):
        super().__init__(parent)
        
        style = ttk.Style()

        style.configure('Treeview',
            font=("Inter", -12,))

        style.configure("Treeview.Heading", font=("Inter", -12, "bold"))

        style.map('Treeview',
            background=[('selected', "#78F292")],
            foreground=[('selected', 'black')]
        )

        self.cols = []
        for col in columns:
            self.cols.append(col[0])

        tree_scroll = ttk.Scrollbar(self)
        self.tree = ttk.Treeview(self, columns=self.cols, show="headings", selectmode="browse", yscrollcommand=tree_scroll.set)
        tree_scroll.config(command=self.tree.yview)

        for col in columns:
            self.tree.column(col[0], width=col[1])
            self.tree.heading(col[0], text=col[0], anchor='w')

        self.tag = 'odd'
        self.tree.tag_configure(tagname='odd', background="#EFEFEF")

        tree_scroll.pack(side='right', fill='y')
        self.tree.pack()

    def return_selctedItem_ID(self):
        return self.tree.item(self.tree.selection(), 'text') 
    
    def return_selctedItem(self):
        return self.tree.item(self.tree.selection(), 'values') 
    
    def delete_selected_item(self):
        self.tree.delete(self.tree.selection())
    
    def insert_entry(self, id, entry):
        self.tree.insert(parent='', index='end', text=id, values=entry, tags=self.tag)
        self.tag = 'even' if self.tag == 'odd' else 'odd'    
 
    def delete_all(self):
        for item in self.tree.get_children():
            self.tree.delete(item)        


class SubmitBtns(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg='white')
        
    def create_btn(self, text,text_color ,btn_color, btns_pad, btn_fun):
        btn_subframe = tk.Frame(self, width=136, height=36)
        btn_subframe.pack_propagate(False)
        btn = tk.Button(btn_subframe, text=text, font=('Inter', -16, "bold"), fg=text_color, bg=btn_color, activeforeground=text_color, activebackground=btn_color , bd=0, command=btn_fun)  
        btn.pack(fill='both', expand=True)
        btn_subframe.pack(padx=(0,btns_pad), side='left')        



