
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Generate some random data
x = np.random.rand(100, 10)
y = np.random.rand(100, 10)

# Perform PCA on the data
pca = PCA(n_components=2)
pca_x = pca.fit_transform(x)
pca_y = pca.fit_transform(y)

# Plot the results
fig, ax = plt.subplots(1, 2, figsize=(10, 6))
ax[0].scatter(pca_x[:, 0], pca_x[:, 1], c=labels)
ax[1].scatter(pca_y[:, 0], pca_y[:, 1], c=labels)

# Add labels to the plots
ax[0].set_xlabel('Principal Component 1')
ax[0].set_ylabel('Principal Component 2')
ax[1].set_xlabel('Principal Component 1')
ax[1].set_ylabel('Principal Component 2')

# Show the plots
plt.show()