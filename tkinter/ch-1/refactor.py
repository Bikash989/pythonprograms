import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()   #create windows instance
win.title("Python GUI") #set title

lbl = ttk.Label(win, text = "Enter a name ") #create a label
lbl.grid(column = 0, row = 0, sticky = tk.W, padx = 2)   # place it in the window frame

lbl2 = ttk.Label(win, text = " Choose a number: ") # create a 2nd label
lbl2.grid(column = 1, row = 0)  # place it in the window frame, right next to the level above

txtbox1Val = tk.StringVar() # create a variable to store textbox1 value
txtbox1 = tk.Entry(win, textvariable = txtbox1Val) #create the textbox and set variable
txtbox1.grid(column = 0, row = 1)  # place it in the window frame

# event handler for button click
def func():
    btn.configure(text = "You Clicked!") # changing the label text of button
btn = ttk.Button(win, text = "Click Me!", command = func) # create a button
btn.grid(column = 2, row = 1)  # place button in the window frame

comboVal = tk.StringVar() # variable to store combobox value
combobox = ttk.Combobox(win, textvariable = comboVal, width = 12, state = 'readonly') # create the combox and made readonly, user can't enter value
combobox['values'] = (1, 2, 4, 6, 100) # setting some values for combobox
combobox.current(0) # display first item from list of values
combobox.grid(column = 1, row = 1) # place the combobox in the window

# 3 checkbox
checkboxVal = tk.IntVar()  # an integer variable
chkbox1 = tk.Checkbutton(win, text = 'disabled', variable = checkboxVal,state = 'disabled') # a disabled checkbox
chkbox1.select()    # make is ticked

checkboxVal2 = tk.IntVar()  # an integer variable
chkbox2 = tk.Checkbutton(win, text = 'UnChecked', variable = checkboxVal2)
chkbox2.deselect() # unselect checkbox default

checkboxVal3 = tk.IntVar() # an integer variable
chkbox3 = tk.Checkbutton(win, text = "Checked", variable = checkboxVal3)
chkbox3.select() # make it checked, variable will be set to 1

# placing all three checkbox in one row, and different columns
chkbox1.grid(column = 0, row = 2, sticky = tk.W)
chkbox2.grid(column = 1, row = 2, sticky = tk.W)
chkbox3.grid(column = 2, row = 2, sticky = tk.W)

# 3 radio Button
colors = ['Blue', 'Red', 'Green'] # declaring a list of colors

# event when radio button is selected
def radCall():
    radSel = radSelect.get()
    if radSel == 0:     # if first radio button is selected, change background color to colors[0]
        win.configure(background = colors[0])
    elif radSel == 1:
        win.configure(background = colors[1])
    elif radSel == 2:
        win.configure(background = colors[2])

radSelect = tk.IntVar(); # an integer variable
radSelect.set(99) # default selected value

for col in range(3): # running thrice and creating and placing radio button in the window frame
    curRad = tk.Radiobutton(win, text = colors[col], variable = radSelect,
                        value = col, command = radCall)
    curRad.grid(column = col, row = 4, sticky = tk.W) # sticky makes sure it aligns

# creating scrolledtext, sort of notepad area
scrol_w = 45    # scroll width
scrol_h = 3     # scroll height
myscroll = scrolledtext.ScrolledText(win, width = scrol_w, height = scrol_h, wrap = tk.WORD) # common mistake, it's not in tk class, instead ScrolledText
myscroll.grid(row = 5, columnspan = 3) # placing the scrolltext in the windows frame



win.mainloop()
