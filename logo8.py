import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the grid
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
xx, yy = np.meshgrid(x, y)

# Print the meshgrid
print(xx)

# Compute the function values
zz = np.sin(xx) + np.sin(yy)

# Create the figure
fig = plt.figure()

# Add a 3D subplot
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(xx, yy, zz, cmap=cm.coolwarm)

# Set the z axis limits
ax.set_zlim(-2.0, 2.0)

# Show the plot
plt.show()
