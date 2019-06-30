import tkinter as tk
from tkinter import scrolledtext

win = tk.Tk()

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width = scrol_w, height = scrol_h, wrap = tk.WORD)
scr.grid(column = 0, columnspan = 3)

# start GUI
win.mainloop()
