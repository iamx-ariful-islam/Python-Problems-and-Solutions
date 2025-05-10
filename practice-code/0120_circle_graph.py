# pip install numpy
# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

# define the circle parameters
r  = 3 # radius
x0 = 1 # x-center
y0 = 1 # y-center

# generate some data
t = np.linspace(0, 2*np.pi, 1000)
x = x0 + r*np.cos(t)
y = y0 + r*np.sin(t)

# create a circle graph
fig, ax = plt.subplots()
ax.plot(x, y)

# add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Circle Graph')

plt.show()