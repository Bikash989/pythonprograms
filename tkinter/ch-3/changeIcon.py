import tkinter as tk
from tkinter import Tk
# from tkinter import ttk

root = tk.Tk() # don't pay attentio nto this now create a window
root.title("PythonGUI")
root.minsize(290, 290)
img = tk.Image("photo", file = "@icon2.ico")
root.tk.call('wm', 'iconphoto', root._w, img)
# root.iconbitmap('@maps-and-flags.png')

root.mainloop()
