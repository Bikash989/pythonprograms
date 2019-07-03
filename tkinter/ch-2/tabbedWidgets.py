import tkinter as tk
from tkinter import ttk
from tkinter import Spinbox
from tkinter import scrolledtext
win = tk.Tk()
win.title("Tabbed Widgets")

tabControl = ttk.Notebook(win) # creates tabl

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = "Tab 1")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = "Tab 2")

tabControl.pack(expand = 1, fill = "both") # pack to make visible

'''
hierarchy, tab -> labelframe -> labelInside
'''
# make a label Frame
mighty = ttk.LabelFrame(tab1, text = "Mighty Python")
mighty.grid(column = 0, row = 0, padx = 8, pady = 20)

# label using mighty as parent
my_label = ttk.Label(mighty, text = "Enter a name:")
my_label.grid(column = 0, row = 0, padx = 20, pady = 20, sticky = 'W')
val = tk.StringVar()
tk.Entry(mighty, textvariable = val).grid(column = 1, row = 0, padx = 10, pady = 10, sticky = 'W')

# spinbox callback
def _spin():
    value = spin.get()
    print(value)
    scrol.insert(tk.INSERT, value + '\n')

# adding a spinbox Widget
spin = Spinbox(mighty, from_ = 0, to = 10, width = 5, bd = 8, command = _spin)
spin.grid(column = 0, row = 2, padx = 10, pady = 10)  # bd-border width

scrol = scrolledtext.ScrolledText(mighty, height = 10, width = 40, wrap = tk.WORD)
scrol.grid(row = 3, columnspan = 4)

my_label2 = ttk.Label(mighty, text = "Choose a number")
my_label2.grid(column = 0, row = 1, padx = 20, pady = 20, sticky = 'W', )

comboval = tk.StringVar()
combo = ttk.Combobox(mighty, textvariable = comboval, state = 'readonly')
combo['values'] = (1,2,3,4,5)
combo.grid(column = 1, row = 1, padx = 14, pady = 20, sticky = 'W')
combo.current(0)

# adding in tab2
about = ttk.LabelFrame(tab2, text = "About")
about.grid(column = 0, row = 0, padx = 8, pady = 20)
ttk.Label(about, text = "Hello it's me bikash das").grid(padx = 20, pady = 10,column = 0, row = 0)
win.mainloop()
