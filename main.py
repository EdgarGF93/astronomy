

from circles import draw_earth, draw_moon, draw_sun, draw_solar_system

import numpy as np
import matplotlib.pyplot as plt


def kk():
    fig, ax = plt.subplots(figsize=(6,6))
    mat = np.array([
        [(50,50,50)]
    ]).astype(int)

    plt.imshow(mat)
    plt.show()




if __name__ == '__main__':
    draw_solar_system()

