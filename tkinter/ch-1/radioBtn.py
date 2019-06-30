import tkinter as tk
from tkinter import ttk

win = tk.Tk()

# some colors
green = 'Green'
blue = 'Blue'
red = 'Red'

# radio button callback
def clickradio():
    radSel = val.get()  # get which radio is selected, value is returned
    if radSel == 1:
        win.configure(background = green)
    elif radSel == 2:
        win.configure(background = blue)
    elif radSel == 3:
        win.configure(background = red)

# tkinter radio button widgets
val = tk.IntVar()
radio1 = ttk.Radiobutton(win, text = 'Green', variable = val, value = 1, command = clickradio)
radio1.grid(column = 0, row = 0)    # sticky aligns to West widget, even if you resize

radio2 = ttk.Radiobutton(win, text = 'blue', variable = val, value = 2, command = clickradio)
radio2.grid(column = 0, row = 1)

radio3 = ttk.Radiobutton(win, text = 'red', variable = val, value = 3, command = clickradio)
radio3.grid(column = 0, row = 2)





# start GUI
win.mainloop()
