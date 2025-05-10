# pip install matplotlib

import matplotlib.pyplot as plt


rows = 5
plt.figure(figsize=(6, 6))

for i in range(rows):
    for j in range(rows-i):
        plt.scatter(j, -i, s=800, c='red')
    
plt.xlim(-0.5, rows-0.5)
plt.ylim(-rows+0.5, 0.5)

plt.axis('off')
plt.gca().set_aspect('equal', adjustable='datalim')
plt.title('Right angled triangle pattern', fontsize=14)
plt.show()