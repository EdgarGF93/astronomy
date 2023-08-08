from data import *
import matplotlib.pyplot as plt

def draw_earth():
    fig, axes = plt.subplots()
    earth = plt.Circle((0, 0.), EARTH_RADIUS_SCALED, color=np.array(EARTH_COLOR) / 255)
    axes.set_aspect(1)
    axes.add_artist(earth)
    plt.title('EARTH')
    plt.xlim([-EARTH_RADIUS_SCALED*2,EARTH_RADIUS_SCALED*2])
    plt.ylim([-EARTH_RADIUS_SCALED*2,EARTH_RADIUS_SCALED*2])
    plt.show()
            

def draw_moon():
    fig, axes = plt.subplots()
    moon = plt.Circle((0, 0.), MOON_RADIUS_SCALED, color=np.array(MOON_COLOR) / 255)
    axes.set_aspect(1)
    axes.add_artist(moon)
    plt.title('MOON')
    plt.xlim([-MOON_RADIUS_SCALED*2,MOON_RADIUS_SCALED*2])
    plt.ylim([-MOON_RADIUS_SCALED*2,MOON_RADIUS_SCALED*2])
    plt.show()

def draw_sun():
    fig, axes = plt.subplots()
    sun = plt.Circle((0, 0.), SUN_RADIUS_SCALED, color=np.array(SUN_COLOR) / 255)
    axes.set_aspect(1)
    axes.add_artist(sun)
    plt.title('SUN')
    plt.xlim([-SUN_RADIUS_SCALED*2,SUN_RADIUS_SCALED*2])
    plt.ylim([-SUN_RADIUS_SCALED*2,SUN_RADIUS_SCALED*2])
    plt.show()


def draw_solar_system():
    fig, axes = plt.subplots()

    sun = plt.Circle((0, 0.), SUN_RADIUS_SCALED, color=np.array(SUN_COLOR) / 255)
    earth = plt.Circle((SUN_EARTH_DISTANCE_SCALED, 0.), EARTH_RADIUS_SCALED, color=np.array(EARTH_COLOR) / 255)
    moon = plt.Circle((SUN_EARTH_DISTANCE_SCALED + EARTH_MOON_DISTANCE_SCALED, 0.), MOON_RADIUS_SCALED, color=np.array(MOON_COLOR) / 255)

    axes.add_artist(sun)
    axes.add_artist(earth)
    # axes.add_artist(moon)
    axes.set_aspect(1)

    plt.xlim([-SUN_RADIUS_SCALED*2,SUN_EARTH_DISTANCE_SCALED*2])
    plt.ylim([-SUN_RADIUS_SCALED*2,SUN_RADIUS_SCALED*2])

    plt.show()