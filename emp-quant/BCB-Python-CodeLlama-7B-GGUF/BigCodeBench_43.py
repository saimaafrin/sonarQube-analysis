
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Replace NaN values with the average of the column
    df = df.fillna(df.mean())

    # Calculate statistics for each numeric column
    stats = df.describe()

    # Create a list of matplotlib Axes objects for each numeric column
    axes = []
    for col in df.select_dtypes(include=['number']).columns:
        ax = sns.distplot(df[col], bins=10)
        axes.append(ax)

    return (stats, axes)