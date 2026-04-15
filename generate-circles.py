import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math
import json
import os

def write_json(target_path, target_file, data): #create and write to subfolder
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    with open(os.path.join(target_path, target_file), 'w') as f:
        json.dump(data, f)

for f in range(100): #loop for generating multiple plots and metadata files

    r = 0.01+0.04*np.random.rand()  # random radius between 0.01 and 0.05

    width = 1 #given domain
    height = 0.8

    rand_x = -r*np.random.rand() #random starting position for the first circle, between -r and 0. uniform distribution inside hexagon would be ideal for uniform randomness.
    rand_y = -r*np.random.rand()

    diag = math.sqrt(width**2 + height**2) #diagonal of the window, to make sure we plot all circles that could be visible in the window, even if they are outside of it

    fig, ax = plt.subplots()

    rand_angle = 2*np.pi*(0.5-np.random.rand())/6 #random angle for the window, one sixth because of reptition of the hexagonal pattern

    json_data = {} #list for collecting metadata

    domain = {
            "offset x": rand_x,
            "offset y": rand_y,
            "width": width,
            "height": height,
            "angle": rand_angle
    }# domain data

    json_data["domain"]=domain #adding domain info to metadata
    circles = [] #circle data

    move_x = rand_x  #setup for while loop
    move_y = rand_y
    mirror_x = rand_x  #mirrored coordinates to plot enough of the hexgrid pattern for angled domains
    mirror_y = rand_y

    rows = 0 #tracking for rows

    while move_y - r < 1.2 * diag:  # -r to plot cutoff circles, factor 1.2 to plot all possible corners.
        while move_x - r < 1.2 * diag:
            if move_x + r > 0 and move_y + r > 0:  # to avoid plotting circles far outside the window
                if move_x - r > 0 and move_y - r > 0 and move_x + r < width and move_y + r < height:  # tracking all circles fully inside the window for metadata
                    circle = plt.Circle((move_x, move_y), r, color='green')  # plotting circles inside the window in green
                    ax.add_patch(circle)
                    circle = {
                        "circle":{
                            "x": move_x,
                            "y": move_y,
                            "radius": r
                        }
                    }
                    circles.append(circle)
                else:
                    circle = plt.Circle((move_x, move_y), r, color='white') #plotting circles outside the window in white
                    ax.add_patch(circle)
                if rows > 0:
                    if mirror_x - r > 0 and mirror_y - r > 0 and mirror_x + r < width and mirror_y + r < height: #as above for mirrored line of construction
                        circle = plt.Circle((mirror_x, mirror_y), r, color='green')
                        ax.add_patch(circle)
                        circle = {
                            "circle":{
                                "x": mirror_x,
                                "y": mirror_y,
                                "radius": r
                            }
                        }
                        circles.append(circle)
                    else:
                        circle = plt.Circle((mirror_x, mirror_y), r, color='white')
                        ax.add_patch(circle)

            move_x += 2*r*np.cos(rand_angle) #rotation matrix to move along hexgrid
            move_y += 2*r*np.sin(rand_angle)
            mirror_x += 2*r*np.cos(rand_angle)
            mirror_y += 2*r*np.sin(rand_angle)

        rows += 1

        move_x = rand_x-rows*r*np.cos(rand_angle)-rows*np.sqrt(3)*r*np.sin(rand_angle) #rotation and direction shift to new line in hexgrid
        move_y = rand_y-rows*r*np.sin(rand_angle)+rows*np.sqrt(3)*r*np.cos(rand_angle)

        mirror_x = rand_x+rows*r*np.cos(rand_angle)+rows*np.sqrt(3)*r*np.sin(rand_angle)
        mirror_y = rand_y+rows*r*np.sin(rand_angle)-rows*np.sqrt(3)*r*np.cos(rand_angle)

    json_data["circles"]=circles #add circle data to metadata

    ax.set_xlim((0, width)) #set domain for plot
    ax.set_ylim((0, height))

    ax.set_facecolor('black') #black background

    write_json('dataset', f'metadata_{f}.json', json_data) #save json to subfolder

    fig.savefig(os.path.join('dataset', f'plotcircles_{f}.png')) #save plot to subfolder
    plt.close()
    print(f'picture and metadata {f} generated')