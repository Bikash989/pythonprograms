"""
A program that stores book information
title, author, publication-year, isbn

user can:
    CRUD:- create, read (whole, based on attributes), update and delete
also search a book
"""
from tkinter import *

class myGui(object):
    """docstring for myGui."""
    def __init__(self):
        self.win = Tk()
        self.win.title("My Book Store")
        self.create_widgets()
        self.start_gui()

    def create_widgets(self):
        l1 = Label(self.win, text = "Title")
        l2 = Label(self.win, text = "Author")
        l3 = Label(self.win, text = "Year")
        l4 = Label(self.win, text = "ISBN")
        l1.grid(row = 0, column = 0)
        l2.grid(row = 0, column = 2)
        l3.grid(row = 1, column = 0)
        l4.grid(row = 1, column = 2)

        title = StringVar()
        author = StringVar()
        year = StringVar()
        isbn = StringVar()
        e1 = Entry(self.win, textvariable = title)
        e2 = Entry(self.win, textvariable = author)
        e3 = Entry(self.win, textvariable = year)
        e4 = Entry(self.win, textvariable = isbn)
        e1.grid(row = 0, column = 1)
        e2.grid(row = 0, column = 3)
        e3.grid(row = 1, column = 1)
        e4.grid(row = 1, column = 3)

        listbox1 = Listbox(self.win, height = 10, width = 35)
        listbox1.grid(row = 2, column = 0, rowspan = 6,columnspan = 2)

        scrol = Scrollbar(self.win, width = 18, troughcolor="blue")
        scrol.grid(row = 2, column = 2, rowspan = 6)

        listbox1.configure(yscrollcommand = scrol.set)
        scrol.configure(command = listbox1.yview) # vertical view

        btn1 = Button(self.win, text = "View all", width = 12)
        btn2 = Button(self.win, text = "Search Book", width = 12)
        btn3 = Button(self.win, text = "Add Book", width = 12)
        btn4 = Button(self.win, text = "Update", width = 12)
        btn5 = Button(self.win, text = "Delete", width = 12)
        btn6 = Button(self.win, text = "Close", width = 12)
        btn1.grid(row = 2, column = 3)
        btn2.grid(row = 3, column = 3)
        btn3.grid(row = 4, column = 3)
        btn4.grid(row = 5, column = 3)
        btn5.grid(row = 6, column = 3)
        btn6.grid(row = 7, column = 3)


    def start_gui(self):
        self.win.mainloop()


draw_layout = myGui()
