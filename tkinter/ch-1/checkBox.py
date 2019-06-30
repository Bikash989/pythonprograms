import tkinter as tk
from tkinter import ttk

win = tk.Tk()

# create checkbox
checkVal = tk.IntVar()
check1 = tk.Checkbutton(win, text = 'Disabled', variable = checkVal, state = 'disabled')
check1.select()
check1.grid(column = 0, row = 0)  # display W

checkVal2 = tk.IntVar()
check2 = tk.Checkbutton(win, text = 'Unchecked', variable = checkVal2)
check2.deselect()   # enforcing to deselect
check2.grid(column = 1, row = 0)

checkVal3 = tk.IntVar()
check3 = tk.Checkbutton(win, text = 'Checked', variable = checkVal3)
check3.select()
check3.grid(column = 3, row = 0)

print(checkVal3.get(), checkVal2.get(), checkVal.get())






# start GUI
win.mainloop()
