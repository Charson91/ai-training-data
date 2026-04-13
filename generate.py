import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math

r = 0.01+0.04*np.random.rand()  # random radius between 0.01 and 0.05
print(r)
width = 1
height = 0.8


fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

rand_angle = 2*np.pi*np.random.rand()/6 #random angle for the window, one sixth because of the hexagonal pattern
print(rand_angle)
#rand_angle = 0

rand_x = r*(1-2*np.random.rand()) #random starting position for the first circle, between -r and r
rand_y = r*(1-2*np.random.rand())
i = rand_x
j = rand_y-math.ceil(r/np.cos(rand_angle))

k = 0 #shift for the first row, to create the hexagonal pattern

while j-r < height: # -r to plot cutoff circles
    while i-r < width:
        circle = plt.Circle((i, j), r, color='white')
        ax.add_patch(circle)
        i += 2*r*np.cos(rand_angle) #hexgrid distance in width
        j += 2*r*np.sin(rand_angle)
    k += 1
    i = rand_x #reset position
    j = rand_y-math.ceil(r/np.cos(rand_angle))
    i += -k*r*np.cos(rand_angle)-k*np.sin(rand_angle)*np.sqrt(3)*r #reset position of the first circle in the next row, shifted by r to create the hexagonal pattern
    j += k*np.sqrt(3)*r*np.cos(rand_angle)-k*r*np.sin(rand_angle) #hexgrid distance in height



ax.set_xlim((0, width))
ax.set_ylim((0, height))

ax.set_facecolor('black')

fig.savefig('plotcircles.png')