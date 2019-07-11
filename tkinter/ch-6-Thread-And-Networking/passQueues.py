import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from threading import Thread
from time import sleep
import Queues as bq

class OOP():
    def __init__(self):
        ''' create instance '''
        self.win = tk.Tk()

        ''' Add a title '''
        self.win.title("Python GUI")
        self.create_widgets()

    ''' method '''
    def create_thread(self):
        self.run_thread = Thread(target = self.method_in_a_thread, args=[8])
        self.run_thread.setDaemon(True)
        self.run_thread.start()     # start the thread

        print(self.run_thread)      # printint out the instance of the thread


    def method_in_a_thread(self, val):
        print('Hi,' + self.name.get() + ' how are you!')
        print('createThread():', self.run_thread.isAlive())
        for idx in range(val):
            val = "printing " + str(idx)
            self.action.configure(text= val)
            sleep(2)
            self.scrol.insert(tk.INSERT, str(idx) + '\n')
        print('createThread():', self.run_thread.isAlive())

    ''' button callback '''
    def click_me(self):
        # self.action.configure(text = 'Hello' + self.name.get())
        # self.create_thread()
        print(self)
        bq.write_to_scrol(self)

    def _spin(self):
        value = self.spin.get() #get the value
        print(value)            #print the value
        self.scrol.insert(tk.INSERT, value + "\n")

    # ... more call back methods

    def create_widgets(self):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text="Tab 1")
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text = "Tab 2")
        # pack to make visible
        tabControl.pack(expand = 1, fill = "both")

        ''' LabelFrame using tab1 as the parent '''
        lf1 = ttk.LabelFrame(tab1, text = 'Label Frame 1')
        lf1.grid(column = 0, row = 0, padx = 8, pady =4)

        ''' Add a label in lf1 '''
        a_label = ttk.Label(lf1, text="Enter a name")
        a_label.grid(column = 0, row = 0, padx = 5, pady = 2)


        ''' Adding a textbox entry widget in labelframe 1'''
        self.name = tk.StringVar()
        name_entered = ttk.Entry(lf1, width = 24, textvariable = self.name)
        name_entered.grid(column = 0, row = 1, sticky = 'W')

        ''' Adding a button in labelframe1'''
        self.action = ttk.Button(lf1, text = "Click Me!", command = self.click_me)
        self.action.grid(column = 2, row = 1)

        ttk.Label(lf1, text="choose a no").grid(column=1, row=0)
        self.number = tk.StringVar()    # all variable name should precede with self
        self.number_chosen = ttk.Combobox(lf1, width = 14, textvariable = self.number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column = 1, row = 1)
        self.number_chosen.current(0)

        ''' Adding a Spinbox widget '''
        self.spin = tk.Spinbox(lf1, values = (1, 2, 4, 42, 100), width = 5, bd = 9, command = self._spin)
        self.spin.grid(column = 0, row = 2, sticky = 'W', padx = 5) # align left (West)

        ''' Adding a scrol text '''
        scrol_w = 40
        scrol_h = 10
        self.scrol = scrolledtext.ScrolledText(lf1, width = scrol_w, height = scrol_h, wrap = tk.WORD)
        self.scrol.grid(column = 0, row =3, sticky = 'WE',columnspan = 3)



oop = OOP()


oop.win.mainloop()
