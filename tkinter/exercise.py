from tkinter import *

def convert():
    kg = 3.34
    grams = kg * 1000
    pounds = kg * 2.20462
    ounces = kg * 35.274
    output = str(round(grams,2)) + " g " + str(round(pounds,2)) + " p " + str(round(ounces,2)) + " o"
    label2 = Label(window, text = output)
    label2.grid(row=1, column = 1)

window = Tk() #new window
#text field to enter number and store in value
value = StringVar() #user entered value
txtField = Entry(window, textvariable = value, width = 20)
txtField.grid(row = 0, column = 1)
 #display message
label = Label(window, text="Enter a number")
label.grid(row = 0, column = 0)

#button with action linked to a function
btn1 = Button(window, text = "Convert" ,command = convert)
btn1.grid(row = 1, column = 0)

#show result


window.mainloop()
