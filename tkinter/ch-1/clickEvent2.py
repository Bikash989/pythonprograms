import tkinter as tk
from tkinter import ttk

# create an instance of window (tk)
win = tk.Tk()   # creates an empty window

# action for button click
def click():
    btn.configure(text = "Hello " + name.get())  # get() to retrive the name from the text field


# create a Label
ttk.Label(win, text = "Enter a name: ").grid(column = 0, row = 0)

# add a Text Box Entry widget, StringVar = string variable (telling beforehand)
name = tk.StringVar()
input = ttk.Entry(win, width = 15, textvariable = name) # width is hardcoded, it will not change
input.grid(column = 0, row = 1)

# add a Button
btn = ttk.Button(win, text = "Click", command = click)
btn.grid(column = 1, row = 1)

input.focus()       # cursor focused in text box

# start the GUI
win.mainloop()
