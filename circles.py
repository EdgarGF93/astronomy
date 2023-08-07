from data import *
import matplotlib.pyplot as plt

def draw_earth():
    fig, axes = plt.subplots()
    earth = plt.Circle((0, 0.), EARTH_RADIUS_SCALED, color=EARTH_COLOR)
    axes.set_aspect(1)
    axes.add_artist(earth)
    plt.title('EARTH')
    plt.xlim([-2,2])
    plt.ylim([-2,2])
    plt.show()
            

def draw_moon():
    fig, axes = plt.subplots()
    moon = plt.Circle((0, 0.), MOON_RADIUS_SCALED, color=MOON_COLOR)
    axes.set_aspect(1)
    axes.add_artist(moon)
    plt.title('MOON')
    plt.xlim([-2,2])
    plt.ylim([-2,2])
    plt.show()
