# pip install matplotlib

import matplotlib.pyplot as plt


sizes  = [10, 25, 20, 15, 35]
labels = ['A', 'B', 'C', 'D', 'E']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()