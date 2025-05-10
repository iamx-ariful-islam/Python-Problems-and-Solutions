# pip install matplotlib

import matplotlib.pyplot as plt


categories = ['A', 'B', 'C', 'D', 'E']
values     = [10, 25, 20, 15, 35]

plt.bar(categories, values, color='blue')
plt.show()