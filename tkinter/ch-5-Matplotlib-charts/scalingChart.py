from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# create the figure
fig = Figure(figsize = (12, 5), facecolor = 'cyan')

axis = fig.add_subplot(111)   # 1 row, 1 column

xValues = [1,2,3,4]

# values to be plotted
a = [6,7.5, 8, 7.5]
b = [5.5, 6.5, 50, 6]   #one value is too high
c = [6.5, 7, 8, 7]

axis.set_ylim(5,8)          # limit the vertical display 5 and max is 8

# plot all three a,b,c w.r.t xValues and save reference to t0, t1 and t2

t0, = axis.plot(xValues, a)  # default color is set, change by specifying color = 'red'
t1, = axis.plot(xValues, b)  # axis.plot(xValues, b, color = 'blue') like this
t2, = axis.plot(xValues, c)  # , is required to create the legend, it turns list into tuples
                             # if you miss comma, code will run, it will plot, but legend will not display


# set label to both axis
axis.set_ylabel('Vertical Label')
axis.set_xlabel('Horizontal Label')

axis.grid()     #default linespace

# set the legend in the figure and specify where to display, -> upper right, lower right ...
fig.legend((t0, t1, t2), ('First line', 'Second line', 'Third line'), 'upper right')

# listener
def _destroyWindow():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

# create canvas to disply the chart
canvas = FigureCanvasTkAgg(fig, master = root)
canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

root.update()
root.deiconify()
root.mainloop()
