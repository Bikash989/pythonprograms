import tkinter as tk
from tkinter import ttk

win = tk.Tk()

label = ttk.Label(win, text = "Enter a name:")
label.grid(column = 0, row = 0)

name = tk.StringVar() # creating a variable of type string
textbox = ttk.Entry(win, textvariable = name)
textbox.grid(column = 1, row = 0)
# Adding a Button and disable it
btn = ttk.Button(win, text = "Disabled Button")
btn.grid(column = 0, row = 1)
btn.configure(state = "disabled")

textbox.focus()  # place mouse cursor












# display GUI
win.mainloop()
