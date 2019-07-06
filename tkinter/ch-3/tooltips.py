# tooltips
import tkinter as tk
from tkinter import scrolledtext
#================================================================
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None
    def show_tip(self, tip_text):
        # "Display text in a tooltip window"
        if self.tip_window or not tip_text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")      # gets size of widget
        x = x + self.widget.winfo_rootx() + 25         # calc to display tooltip
        y = y + cy + self.widget.winfo_rooty() + 25     # below and to the right
        self.tip_window = tw = tk.Toplevel(self.widget) # create new tooltip window
        tw.wm_overrideredirect(True)                    # remove all Window Manager (wm) decorations
        tw.wm_geometry("+%d+%d" % (x, y))                # create window size

        label = tk.Label(tw, text = tip_text, justify=tk.LEFT,
            background="#ffffe0", relief = tk.SOLID, bd = 1,
            font=("tahoma","8","normal"))
        label.pack(ipadx=1)
    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()

#=======================================================================
def create_ToolTip(widget, text):
    toolTip = ToolTip(widget)       # create instance of class
    def enter(event):
        toolTip.show_tip(text)
    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>', enter)   # bind mouse events
    widget.bind('<Leave>', leave)

#====================================================================
win = tk.Tk()
win.title("ToolTip")
spin = tk.Spinbox(win, values=(1,2,3,4,5))
spin.grid(column = 0, row = 0)
# Add a toolTip
create_ToolTip(spin, "This is a Spin Control")

# using a scrolled text control
scrol_w = 30
scrol_h = 3
scrol = scrolledtext.ScrolledText(win, width = scrol_w, height = scrol_h, wrap = tk.WORD)
scrol.grid(column = 0, row = 1, sticky='WE', columnspan = 3)
create_ToolTip(scrol, 'Enter your complain here')
win.mainloop()
