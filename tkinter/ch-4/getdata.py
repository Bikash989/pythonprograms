import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Get Data")

def _spin():
    strData = tk.StringVar()
    strData = spin.get()
    print("Spinbox values: " + strData)

spin = tk.Spinbox(win, values=(0,1,2,3,4,50,100), width = 5, bd = 20,command = _spin, fg = "Red")
spin.grid(column = 0, row = 0)

x = tk.StringVar()
txt = tk.Entry(win, textvariable = x).grid(column = 0, row = 1)

win.mainloop()
