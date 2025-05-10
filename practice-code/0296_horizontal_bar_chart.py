# pip install matplotlib

import matplotlib.pyplot as plt


categories = ['A', 'B', 'C', 'D', 'E']
values     = [10, 15, 20, 25, 35]

plt.barh(categories, values, color='purple')
plt.show()