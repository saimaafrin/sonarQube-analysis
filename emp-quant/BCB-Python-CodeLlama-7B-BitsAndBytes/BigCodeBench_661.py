
import pandas as pd
import seaborn as sns
import numpy as np

# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']

# Create a sample dataframe
df = pd.DataFrame({'x': np.arange(1, 10), 'y': np.arange(1, 10), 'labels': np.random.choice(LABELS, 10)})

# Create a heatmap
ax = sns.heatmap(df, annot=True, cmap='coolwarm')

# Add labels to the heatmap
for i, j, label in zip(df['x'], df['y'], df['labels']):
    ax.text(i, j, label, ha='center', va='center')

# Show the plot
plt.show()