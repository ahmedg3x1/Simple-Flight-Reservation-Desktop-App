import tkinter as tk
from tkinter import messagebox

class BookingPage(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x615")
        self.resizable(False, False)
        self.configure(bg='white')
        tk.Label(self, text="Booking Page", fg="#3E23D6", font=('Inter', -32), bg='white').pack(pady=(40, 10))
        fields = ['Name', 'Flight Number', 'Departure', 'Destination', 'Date', 'Seat Number']

        Form(self, fields, 'Book')
    
class Form(tk.Frame):
    def __init__(self, parent, fields, btn_text):
        super().__init__(parent)
        self.parent = parent
        self.configure( width=292, bg='white')
        self.pack_propagate(False)
        self.entrys = self.create_fields(fields)
        self.create_submit_btns(btn_text)
        self.pack(fill='y', expand=True)

    def create_fields(self, fields):
        entrys = []
        for field in fields:
            tk.Label(self, text=f"{field}:", font=('Inter', 11, "bold"), bg='white').pack(anchor="w", pady=(8, 0))
            entry = tk.Entry(self, font=('Arial', 12), bg='#D9D9D9', bd=0)
            entry.pack(fill='x', ipady=8)
            entrys.append(entry) 
        return entrys
    
    def create_submit_btns(self, btn_text):
        btn_frame = tk.Frame(self, width=292, height=36, bg='white')
        btn_frame.pack_propagate(False)
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text=btn_text, font=('Inter', -20, "bold"), fg='white', bg='#4492F7', activeforeground='white', activebackground='#4492F7', bd=0, command=self.submit, width=11).pack(side='left')           
        tk.Button(btn_frame, text='Cancel', font=('Inter', -20, "bold"), fg='white', bg="#EC2929", activeforeground='white', activebackground='#EC2929', bd=0, command=self.cancel, width=11).pack(side='right')           

    def submit(self):
        messagebox.showinfo(message='The Operation was successful', parent=self)
        for entry in self.entrys:
            print(entry.get())
            entry.delete(0, tk.END)
        self.entrys[0].focus_set()
    
    def cancel(self):
        self.parent.destroy()