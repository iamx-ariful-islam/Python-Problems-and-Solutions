# pip install numpy
# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 50)
y = np.sin(x)

plt.scatter(x, y, color='g', marker='x')
plt.show()