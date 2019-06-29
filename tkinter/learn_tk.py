from tkinter import *

window = Tk()
def add10():
    val = float(value.get()) + 10
    t1.insert(END, val)  # Text() has a method insert

btn1 = Button(window, text = "Click", command = add10) #linking btn to display func
# btn1.pack()
btn1.grid(row = 0, column = 0)

value = StringVar()
textbox1 = Entry(window, textvariable = value)
textbox1.grid(row=0, column = 1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 2)
window.mainloop()
