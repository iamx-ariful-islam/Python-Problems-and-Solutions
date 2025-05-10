# pip install numpy
# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt


random_data = np.random.randn(1000)
plt.hist(random_data, bins=30, color='orange')
plt.show()