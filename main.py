import tkinter as tk
from database import Database
from home import HomePage

db = Database()



mainWindow = tk.Tk()
icon = tk.PhotoImage(file='assets/App.png')
mainWindow.iconphoto(True, icon)

mainWindow.title('Flight Reservation Desktop App')
HomePage(mainWindow, db)

mainWindow.mainloop()
db.close()