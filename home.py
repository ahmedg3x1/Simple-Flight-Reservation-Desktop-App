import os
import tkinter as tk
from PIL import Image, ImageTk
from booking import BookingPage

class HomePage(tk.Frame):
        def __init__(self, parent, db):
            super().__init__(parent)
            self.parent = parent
            self.db = db
            self.configure(bg='white')
            tk.Label(self, text="Welcome to Flight Reservations App", font=('Inter', -32, 'bold'), fg= '#3E23D6', bg='white').pack(pady=30)

            cardContiner = tk.Frame(self, bg='white')
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=1)

            text = 'Reserve your next flight by providing your details and flight information.'   
            img1 = os.path.join(os.path.dirname(__file__), 'assets', 'book_flight_img.png') 
            CardWidget(cardContiner, 0, 0, img1, 'Book a Flight', text, 'Book a Flight', self.book_flight)
            
            text2 = 'Manage your existing reservations, view details, edit or cancel if needed.'    
            img2 = os.path.join(os.path.dirname(__file__), 'assets', 'view_reservations_img.png') 
            CardWidget(cardContiner, 0, 1, img2, 'View Reservations', text2, 'View Reservations', self.view_reservation)
            cardContiner.pack()
            self.pack()


        def book_flight(self):
            BookingPage(self.parent, self.db).grab_set()

        def view_reservation(self):
            self.parent.change_frame('ReservationsPage')

class CardWidget(tk.Frame):
        def __init__(self, parent, row, col, img_path, title, text, btn_txt, btn_fun):
            super().__init__(parent)
            self.configure(bg='white', bd =1, relief='solid', width=286, height=255)
            self.pack_propagate(False)
            self.grid(row=row, column=col, sticky='e', padx=37)

            self.img =  ImageTk.PhotoImage(Image.open(img_path).resize((92, 92)))
            tk.Label(self, bd=0, image=self.img).pack(pady=12)

            tk.Label(self, text=title, font=('Inter', -18, 'bold'), fg= '#563DE2', bg='white').pack()
            tk.Label(self, text=text, font=('Inter', -13), bg='white', wraplength=243).pack()

            btn_frame = tk.Frame(self, width=187, height=39)
            btn_frame.pack_propagate(False)
            btn = tk.Button(btn_frame, text=btn_txt, font=('Inter', -16, "bold"), fg='white', bg='#4492F7', activeforeground='white', activebackground='#4492F7' , bd=0, command=btn_fun)  
            btn.pack(fill='both', expand=True)
            btn_frame.pack(pady=6)