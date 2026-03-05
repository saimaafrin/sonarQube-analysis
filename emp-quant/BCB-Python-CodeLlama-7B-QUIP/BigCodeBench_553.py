
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(a, b):
    # Generate DataFrame
    data = pd.DataFrame(np.random.rand(len(a), len(b)), index=a, columns=b)
    # Plot DataFrame
    ax = plt.bar(data)
    return ax