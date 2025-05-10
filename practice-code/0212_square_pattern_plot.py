# pip install matplotlib

import matplotlib.pyplot as plt


n = 4
plt.figure(figsize=(5, 5))

for i in range(4):
    for j in range(4):
        plt.scatter(j, -i, s=500, c='orange')

plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Square Pattern Plot', fontsize=14)
plt.show()