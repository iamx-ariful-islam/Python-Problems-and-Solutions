# pip install matplotlib

import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey


Sankey(flows=[1, -1], labels=['Input', 'Output']).finish()
plt.show()