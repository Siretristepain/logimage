import numpy as np
import matplotlib.pyplot as plt

values = np.array([
    [1,0,1,0,0],
    [0,0,0,1,1],
    [1,0,1,1,0],
    [0,1,1,0,0],
])

fig, ax = plt.subplots()
im = ax.imshow(values)

for j in range(len(values[0])):
    for i in range(len(values)):
        text =  ax.text(j, i, values[i, j], ha="center", va="center", color="w")

fig.tight_layout()
plt.show()