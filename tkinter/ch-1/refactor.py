import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Python GUI")

lbl = ttk.Label(win, text = "Enter a name ")
lbl.grid(column = 0, row = 0)

lbl2 = ttk.Label(win, text = " Choose a number: ")
lbl2.grid(column = 1, row = 0)

txtbox1Val = tk.StringVar()
txtbox1 = tk.Entry(win, textvariable = txtbox1Val)
txtbox1.grid(column = 0, row = 1)

def func():
    btn.configure(text = "You Clicked!")
btn = ttk.Button(win, text = "Click Me!", command = func)
btn.grid(column = 2, row = 1)

comboVal = tk.StringVar()
combobox = ttk.Combobox(win, textvariable = comboVal, width = 12, state = 'readonly')
combobox['values'] = (1, 2, 4, 6, 100)
combobox.current(0)
combobox.grid(column = 1, row = 1)

# 3 checkbox
checkboxVal = tk.IntVar()
chkbox1 = tk.Checkbutton(win, text = 'disabled', variable = checkboxVal,state = 'disabled', )
chkbox1.select()

checkboxVal2 = tk.IntVar()
chkbox2 = tk.Checkbutton(win, text = 'UnChecked', variable = checkboxVal2)
chkbox2.deselect()

checkboxVal3 = tk.IntVar()
chkbox3 = tk.Checkbutton(win, text = "Checked", variable = checkboxVal3)
chkbox3.select()

chkbox1.grid(column = 0, row = 2)
chkbox2.grid(column = 1, row = 2)
chkbox3.grid(column = 2, row = 2)

# 3 radio Button
colors = ['Blue', 'Red', 'Green']

def radCall():
    radSel = radSelect.get()
    if radSel == 0:
        win.configure(background = colors[0])
    elif radSel == 1:
        win.configure(background = colors[1])
    elif radSel == 2:
        win.configure(background = colors[2])

radSelect = tk.IntVar();
radSelect.set(99)

for col in range(3):
    curRad = tk.Radiobutton(win, text = colors[col], variable = radSelect,
                        value = col, command = radCall)
    curRad.grid(column = col, row = 4, sticky = tk.W)

# creating scrolledtext, sort of notepad area
scrol_w = 45    # scroll width
scrol_h = 3     # scroll height
myscroll = scrolledtext.ScrolledText(win, width = scrol_w, height = scrol_h, wrap = tk.WORD)
myscroll.grid(row = 5, columnspan = 3)



win.mainloop()
