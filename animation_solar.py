import matplotlib.pyplot as plt
from ampl_toolkits.mplot3d import Axes3D
import numpy as np

# Data for celestial bodies (distance from the Sun in astronomical units)
# This data is not to scale and is just for illustration purposes
bodies = {
    "Sun": 0,
    "Mercury": 0.39,
    "Venus": 0.72,
    "Earth": 1,
    "Mars": 1.52,
    "Jupiter": 5.20,
    "Saturn": 9.58,
    "Uranus": 19.22,
    "Neptune": 30.05
}

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each celestial body
for body, distance in bodies.items():
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)
    x = distance * np.outer(np.cos(theta), np.sin(phi))
    y = distance * np.outer(np.sin(theta), np.sin(phi))
    z = distance * np.outer(np.ones(np.size(theta)), np.cos(phi))
    ax.plot_surface(x, y, z, color='c', alpha=0.2)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Solar System')

plt.show()
