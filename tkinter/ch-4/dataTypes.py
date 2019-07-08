import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("400x400")
win.title("Getting Val from Widgets")

''' Available Types
    two methods set and get, using get return 0 for default
    default values of types : PY_VAR
'''

str = tk.StringVar()
str.set("bikash")
print(str.get())

intVar = tk.IntVar()
dbVar = tk.DoubleVar()
blVar = tk.BooleanVar()


# win.mainloop()
