# pip install cartopy
# pip install matplotlib

import cartopy.crs as ccrs
import matplotlib.pyplot as plt


fig, ax = plt.subplots(subplot_kw={"projection": ccrs.Robinson()})
ax.coastlines()

plt.title('Robinson Projection')
plt.show()