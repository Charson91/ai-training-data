import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math
import json

r = 0.01+0.04*np.random.rand()  # random radius between 0.01 and 0.05
#r= 0.04
print(r)

width = 1
height = 0.8

diag = math.sqrt(width**2 + height**2)

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

rand_angle = 2*np.pi*(0.5-np.random.rand())/6 #random angle for the window, one sixth because of reptition of the hexagonal pattern
print(rand_angle)
#rand_angle = 1*np.pi/6
rand_angle = 0.35138543660823046

rand_x = r*(1-2*np.random.rand()) #random starting position for the first circle, between -r and r
rand_y = r*(1-2*np.random.rand())
i = rand_x
j = rand_y
im = i
jm = j

p = np.random.rand() #density
p = 1

k = 0 #tracking for rows

while j-r < 1.2*diag: # -r to plot cutoff circles, factor 1.2 to plot all possible corners.
    while i-r < 1.2*diag:
        if i + r > 0 and j + r > 0: #to avoid plotting circles far outside the window
            if np.random.rand() <= p: #random generation of metadata
            #if i - r > 0 and j - r > 0 and  i + r < width and j + r < height:
                circle = plt.Circle((i, j), r, color='green')
                ax.add_patch(circle)
            else:
                circle = plt.Circle((i, j), r, color='white')
                ax.add_patch(circle)
        #circle = plt.Circle((im, jm), r, color='blue')
            if np.random.rand() <= p: #mirrored circles for angled plots
              circle = plt.Circle((im, jm), r, color='blue')
              ax.add_patch(circle)
            else:
              circle = plt.Circle((im, jm), r, color='blue')
              ax.add_patch(circle)

        i += 2*r*np.cos(rand_angle) #hexgrid distance in width
        j += 2*r*np.sin(rand_angle)
        im += 2*r*np.cos(rand_angle) #hexgrid distance in width
        jm += 2*r*np.sin(rand_angle)

    k += 1
    i = rand_x #reset position
    j = rand_y
    im = i
    jm = j

    i += -k*r*np.cos(rand_angle) #shift x position of new line because of hexgrid
    j += -k*r*np.sin(rand_angle)
    j += k*np.sqrt(3)*r*np.cos(rand_angle) #shift y position of new line because of hexgrid
    i += -k*np.sqrt(3)*r*np.sin(rand_angle) 
    
    im += k*r*np.cos(rand_angle)
    jm += k*r*np.sin(rand_angle)
    jm += -k*np.sqrt(3)*r*np.cos(rand_angle)
    im += k*np.sqrt(3)*r*np.sin(rand_angle)
    print(k, i, j)

 

ax.set_xlim((0, width))
ax.set_ylim((0, height))

ax.set_facecolor('black')

fig.savefig('plotcircles.png')