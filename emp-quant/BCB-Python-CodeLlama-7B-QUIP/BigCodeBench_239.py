
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(original):
    # Extract numeric values from the tuples
    numeric_values = [x[1] for x in original]

    # Compute basic statistics
    stats = np.array(numeric_values).stats()
    mean = stats.mean()
    std = stats.std()
    min = stats.min()
    max = stats.max()

    # Generate histogram with overlaid PDF
    hist, bins = np.histogram(numeric_values, bins=50, density=True)
    plt.hist(bins, hist, alpha=0.6, label=f"PDF\nmean={mean:.2f}, std={std:.2f}, min={min:.2f}, max={max:.2f}")
    plt.show()

    return {
        "np.array": np.array(numeric_values),
        "dict": stats,
        "Axes": plt.gca(),
    }