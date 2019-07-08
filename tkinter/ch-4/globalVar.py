'''
 imports
'''
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep

GLOBAL_CONST = 42

win = tk.Tk()
win.title("Using global")
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
print(str(screen_width) + "x" + str(screen_height))
# winSize = str(screen_width) + "x" + str(screen_height)
# win.geometry(winSize)

def usingGlobal():
    global GLOBAL_CONST
    print(GLOBAL_CONST)
    GLOBAL_CONST = 20
    print(GLOBAL_CONST)

usingGlobal()
print(GLOBAL_CONST)


# win.mainloop()
