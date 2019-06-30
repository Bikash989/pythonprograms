import tkinter as tk
from tkinter import ttk      # contains advanced widget, themed tk

#create instance of Tk class
win = tk.Tk()

#Add a title
win.title("A title")

# Disabling resizing of window
# win.resizable(False, False) # both dimesnion x,y -> false

# Adding a Label
lb1 = ttk.Label(win, text = "This is a Label")
lb1.grid(column = 0, row = 0)

# Button Click Event Function
def clicked():
    action.configure(text = "Click me!")
    lb1.configure(foreground = 'red')
    lb1.configure(text = 'This is a Label')

# Adding a Button
action = ttk.Button(win, text = "Click Me!", command = clicked) # binded to clicked()
action.grid(column = 1, row = 0)



# start GUI
win.mainloop()
