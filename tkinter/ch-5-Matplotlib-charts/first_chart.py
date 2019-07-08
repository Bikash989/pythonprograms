import numpy as np
import matplotlib.pyplot as plt
from pylab import show

x = np.arange(0,10,0.1)
print(x)
y = np.sin(x)
print(y)
print(np.sin(90))
print(np.sin(0))
plt.plot(x,y)
show()
