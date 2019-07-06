import tkinter as tk
from tkinter import ttk
import time
win = tk.Tk()
win.geometry("300x300")
win.title("Progress Bar")
frame = tk.LabelFrame(win, text = "Progress Bar", fg = "Blue")
frame.grid(column = 0, row = 0, padx = 10, pady = 10)

def run_progressbar():
    pb["maximum"] = 100
    for i in range(101):
        time.sleep(0.05)
        progress_bar["value"] = i   # increment progressbar
        pb.update()       # have to call update() in loop
    progress_bar["value"] = 0       # reset/clear progressbar
def start_progressbar():
    pb.start()

def stop_progressbar():
    pb.stop()
def progressbar_stop_after(wait_ms = 1000):
    win.after(wait_ms, pb.stop)
# Add 4 button to frame
ttk.Button(frame, text = "Run Progressbar", command = run_progressbar).grid(column = 0, row = 0, padx = 15, pady = 8)
ttk.Button(frame, text = "Start Progressbar", command = start_progressbar).grid(column = 0, row = 1, padx = 15, pady = 8)
ttk.Button(frame, text = "Stop Immediately", command = stop_progressbar).grid(column = 0, row = 2, padx = 15, pady = 8)
ttk.Button(frame, text = "Stop after second", command = progressbar_stop_after).grid(column = 0, row = 3, padx = 15, pady = 8)

''' add progress bar '''
pb = ttk.Progressbar(win, orient = 'horizontal', length = 286, mode = 'determinate')
pb.grid(column = 0, row = 4, pady = 5, padx = 2)


win.mainloop()
