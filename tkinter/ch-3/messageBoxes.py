import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

win = tk.Tk()
win.title('demo messagebox')

def _msgBox():
    # msg.showinfo('title', 'description')
    # msg.showinfo('Inserted', 'New Record Inserted Successfully')
    # msg.showwarning('Inserted', 'Unable to commit data to database')
    # msg.showerror('Python Error messagebox', 'Error: Close the application by clicking ok')
    response = msg.askyesnocancel('Yes No Cancel', 'Please select your appropriate response')
    print(response)  # Yes = True, No = False, Cancel = None
    if response == True:
        print("You clicked Yes ")
    elif response == False:
        print("You clicked No")
    else:
        print("you clicked Cancel")

menu_bar = Menu(win)
win.config(menu = menu_bar)

help_menu = Menu(menu_bar, tearoff = 0)
help_menu.add_command(label="About", command = _msgBox)
menu_bar.add_cascade(label = "Help", menu = help_menu)

win.mainloop()
