import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

r = 0.01+0.04*np.random.rand(1)  # random radius between 0.01 and 0.05
print(r)

circle1 = plt.Circle((0, 0), 0.2, color='black')
circle2 = plt.Circle((0.5, 0.5), 0.2, color='black')
circle3 = plt.Circle((1, 1), 0.3, color='black') 

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

ax.set_xlim((0, 1))
ax.set_ylim((0, 0.8))

ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)

fig.savefig('plotcircles.png')