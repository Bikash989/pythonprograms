import tkinter as tk
from tkinter import ttk

win = tk.Tk()

ttk.Label(win, text = "Choose a number").grid(column = 1, row = 0)

# combo box widget
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width = 12, textvariable = number, state = 'readonly') # you cannot enter your values
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column = 0, row = 0)
number_chosen.current(0)

print(number_chosen.get())



# start GUI
win.mainloop()
