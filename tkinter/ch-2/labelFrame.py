import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python Gui")
# create legends
button_frame = ttk.LabelFrame(win, text = ' Labels in a Frame')

button_frame.grid(column = 0, row = 0, padx = 20, pady = 40)  # add padding

# place label in the legends
ttk.Label(button_frame, text = "my_label1").grid(column = 0, row = 0, sticky = tk.W)
ttk.Label(button_frame, text = "my_label2").grid(column = 0, row = 1, sticky = tk.W)
ttk.Label(button_frame, text = "my_label3").grid(column = 0, row = 2, sticky = tk.W)

# ttk.Entry(button_frame, width = 20).grid(column = 4, row = 4)
# add padding to all widgets inside legend frame
# winfo_children() returns list of all children inside button_frame
for child in button_frame.winfo_children():
    child.grid_configure(padx = 8, pady = 4)

# display GUI
win.mainloop()
