import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

# create instance
win = tk.Tk()
win.title("Menu")

def _quit():
    win.quit()
    win.destroy()
    exit()

# creating menu bar
menu_bar = Menu(win)
win.config(menu = menu_bar)                 # configure our menu to use win

# create menu and add menu items
file_menu = Menu(menu_bar, tearoff = 0)                 # create file menu, tearoff removes the default line that appears
file_menu.add_command(label = "New")                    # add item
file_menu.add_separator()                               # add separator between items
file_menu.add_command(label = "Exit", command = _quit)
menu_bar.add_cascade(label = "File", menu = file_menu)  # add file menu to menu bar and give it a label

# create another menu_bar
help_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label = "About")

win.mainloop();
