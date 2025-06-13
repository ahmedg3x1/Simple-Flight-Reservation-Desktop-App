import tkinter as tk
from database import Database
from home import HomePage
from reservations import ReservationsPage

class App(tk.Tk):
    def __init__(self, db):
        super().__init__()
        self.geometry("840x420")
        self.resizable(False, False)
        self.configure(bg='white')
        self.columnconfigure(0, weight=1)
        
        self.title('Flight Reservation Desktop App')
        icon = tk.PhotoImage(file='assets/App.png')
        self.iconphoto(True, icon)

        self.frames = {}
        self.frames['HomePage'] = HomePage(self, db)
        self.frames['ReservationsPage'] = ReservationsPage(self, db)

        for frame in self.frames:
            self.frames[frame].grid(row=0, column=0)

        self.change_frame('HomePage')
        
    def change_frame(self, frame):
        self.frames[frame].tkraise()
        if  frame == 'ReservationsPage':
            self.frames[frame].reset()

db = Database()
app = App(db)
app.mainloop()
db.close()
