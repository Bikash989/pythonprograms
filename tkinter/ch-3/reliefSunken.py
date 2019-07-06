import tkinter as tk
from tkinter import ttk
master = tk.Tk()

# w = tk.Spinbox(master, from_=0, to=10, relief = tk.GROOVE, fg = "Red", font = "sans-serif")
w = tk.Spinbox(master, values=(0,50,100), width = 5, bd = 20, relief = tk.RIDGE, fg = "Red")
w.grid(column = 0, row = 0)

master.mainloop()
