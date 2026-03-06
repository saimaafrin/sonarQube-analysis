
import pandas as pd
import matplotlib.pyplot as plt

# Define the matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Define the colormap and interpolation parameters
cmap = 'hot'
interpolation = 'nearest'

# Create the Axes object
fig, ax = plt.subplots()

# Plot the heatmap
ax.imshow(matrix, cmap=cmap, interpolation=interpolation)

# Set the title and labels
ax.set_title('Heatmap of the Matrix')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

# Show the plot
plt.show()