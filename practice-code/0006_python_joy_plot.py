# pip install joypy
# pip install pandas
# pip install matplotlib

import joypy
import pandas as pd
from matplotlib import pyplot as plt


# create a dataset of random numbers
data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})

# create the joy plot
fig, axis = joypy.joyplot(data, ylim='own')

# add labels and title

plt.xlabel('Values')
plt.ylabel('Variables')
plt.title('Joy plot of two variables')

# show the plot
plt.show()