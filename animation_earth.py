from vpython import sphere, vector, rate, color

# Create a central sun object
sun = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.yellow)

# Create planets
mercury = sphere(pos=vector(0.4, 0, 0), radius=0.05, color=color.magenta)
venus = sphere(pos=vector(0.7, 0, 0), radius=0.07, color=color.orange)
earth = sphere(pos=vector(1, 0, 0), radius=0.07, color=color.blue)
mars = sphere(pos=vector(1.5, 0, 0), radius=0.06, color=color.red)

# Set initial velocities of planets
mercury.velocity = vector(0, 0.3, 0)
venus.velocity = vector(0, 0.25, 0)
earth.velocity = vector(0, 0.2, 0)
mars.velocity = vector(0, 0.15, 0)

# Animation loop
while True:
    rate(60)  # Set the frame rate

    # Update positions of planets
    mercury.pos += mercury.velocity
    venus.pos += venus.velocity
    earth.pos += earth.velocity
    mars.pos += mars.velocity

    # Rotate planets around the sun
    mercury.rotate(angle=0.03, axis=vector(0, 1, 0), origin=sun.pos)
    venus.rotate(angle=0.02, axis=vector(0, 1, 0), origin=sun.pos)
    earth.rotate(angle=0.015, axis=vector(0, 1, 0), origin=sun.pos)
    mars.rotate(angle=0.01, axis=vector(0, 1, 0), origin=sun.pos)
