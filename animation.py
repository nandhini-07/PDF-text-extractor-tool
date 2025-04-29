import vpython
from vpython import *

# Function to create a planet
def create_planet(pos, radius, color):
    return sphere(pos=pos, radius=radius, color=color)

# Function to create an orbit path
def create_orbit(pos):
    return curve(pos=[pos, pos])

# Create a 3D scene
scene = canvas(title='Solar System')

# Create the Sun
sun = sphere(pos=vector(0, 0, 0), radius=10, color=color.yellow)

# Create the planets
planets = [
    create_planet(pos=vector(0.39, 0, 0), radius=0.04, color=color.gray(0.7)),
    create_planet(pos=vector(0.72, 0, 0), radius=0.1, color=color.orange),
    create_planet(pos=vector(1, 0, 0), radius=0.1, color=color.blue),
    create_planet(pos=vector(1.52, 0, 0), radius=0.08, color=color.red),
    create_planet(pos=vector(5.2, 0, 0), radius=0.5, color=color.orange),
    create_planet(pos=vector(9.54, 0, 0), radius=0.4, color=color.orange),
    create_planet(pos=vector(19.2, 0, 0), radius=0.3, color=color.cyan),
    create_planet(pos=vector(30.06, 0, 0), radius=0.3, color=color.blue),
]

# Create the orbits
orbits = [
    create_orbit(pos=vector(0.39, 0, 0)),
    create_orbit(pos=vector(0.72, 0, 0)),
    create_orbit(pos=vector(1, 0, 0)),
    create_orbit(pos=vector(1.52, 0, 0)),
    create_orbit(pos=vector(5.2, 0, 0)),
    create_orbit(pos=vector(9.54, 0, 0)),
    create_orbit(pos=vector(19.2, 0, 0)),
    create_orbit(pos=vector(30.06, 0, 0)),
]

# Set up the camera
scene.camera.pos = vector(2, 2, 2)
scene.camera.axis = vector(-2, -2, -2)

while True:
    rate(60)
