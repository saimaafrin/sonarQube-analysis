
import pandas as pd
import seaborn as sns
def task_func(data):
    # Create a correlation matrix heatmap
    heatmap = sns.heatmap(data.corr(), annot=True, cmap='viridis')
    heatmap.set_title('Correlation Matrix')
    return heatmap