import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math
import json


for f in range(10): #loop for generating multiple plots and metadata files
    r = 0.01+0.04*np.random.rand()  # random radius between 0.01 and 0.05
    #r= 0.039816790268998155
    print(r)

    width = 1 #given domain
    height = 0.8

    p = np.random.rand() #density
    p = 1

    rand_x = r*(-np.random.rand()) #random starting position for the first circle, between -r and r. uniform distribution inside hexagon would be ideal for uniform randomness.
    rand_y = r*(-np.random.rand())
    #rand_x = -0.03929876177558801
    ##rand_y = 0.0309872611401763


    diag = math.sqrt(width**2 + height**2) #diagonal of the window, to make sure we plot all circles that could be visible in the window, even if they are outside of it

    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    # (or if you have an existing figure)
    # fig = plt.gcf()
    # ax = fig.gca()

    rand_angle = 2*np.pi*(0.5-np.random.rand())/6 #random angle for the window, one sixth because of reptition of the hexagonal pattern
    #print(rand_angle)
    #rand_angle = 1*np.pi/6
    #rand_angle = 0.3004638311493413

    json_data = {} #list for collecting metadata

    domain = {
            "offset x": rand_x,
            "offset y": rand_y,
            "width": width,
            "height": height,
            "angle": rand_angle
    }# domain data

    json_data["domain"]=domain #adding domain info to metadata
    circles = []

    i = rand_x  #setup for while loop
    j = rand_y
    im = i      #mirrored coordinates because of grid path
    jm = j

    k = 0 #tracking for rows

    while j-r < 1.2*diag: # -r to plot cutoff circles, factor 1.2 to plot all possible corners.
        while i-r < 1.2*diag:
            if i + r > 0 and j + r > 0: #to avoid plotting circles far outside the window
                if i - r > 0 and j - r > 0 and i + r < width and j + r < height: #collecting all circles fully inside the window for metadata
                    if np.random.rand() <= p: #random generation of metadata based on density p
                        circle = plt.Circle((i, j), r, color='green')
                        ax.add_patch(circle)
                        circle = {
                            "circle":{
                                "x": i,
                                "y": j,
                                "radius": r
                            }
                        }
                        circles.append(circle)
                    else:
                        circle = plt.Circle((i, j), r, color='red')
                        ax.add_patch(circle)
                        circle = {
                            "circle":{
                                "x": i,
                                "y": j,
                                "radius": r
                            }
                        }
                else:
                    circle = plt.Circle((i, j), r, color='white')
                    ax.add_patch(circle)
                if k > 0:
                    if im - r > 0 and jm - r > 0 and im + r < width and jm + r < height:
                        if np.random.rand() <= p: #mirrored circles for angled plots
                            circle = plt.Circle((im, jm), r, color='green')
                            ax.add_patch(circle)
                            circle = {
                                "circle":{
                                    "x": im,
                                    "y": jm,
                                    "radius": r
                                }
                            }
                            circles.append(circle)
                        else:
                            circle = plt.Circle((im, jm), r, color='blue')
                            ax.add_patch(circle)
                            circle = {
                                "circle":{
                                    "x": im,
                                    "y": jm,
                                    "radius": r
                                }
                            }
                    else:
                        circle = plt.Circle((im, jm), r, color='white')
                        ax.add_patch(circle)

            i += 2*r*np.cos(rand_angle) #hexgrid distance in width
            j += 2*r*np.sin(rand_angle)
            im += 2*r*np.cos(rand_angle) #hexgrid distance in width
            jm += 2*r*np.sin(rand_angle)

        k += 1
        i = rand_x #reset positions
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
        #print(k, i, j)

    json_data["circles"]=circles

    with open(f'metadata_{f}.json', 'w') as file:
        json.dump(json_data, file, indent=4)
    #print(json_data)

    ax.set_xlim((0, width))
    ax.set_ylim((0, height))

    ax.set_facecolor('black')

    fig.savefig(f'plotcircles_{f}.png')