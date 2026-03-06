
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
COLUMNS = ['Name', 'Age', 'Country', 'Score']

def task_func(df):
    # Check if the input is a valid DataFrame
    if not isinstance(df, pd.DataFrame):
        return "Invalid input"

    # Extract the unique names from the DataFrame
    unique_names = df['Name'].unique()

    # Create a histogram of scores
    hist_fig = plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x='Score', hue='Name', multiple='stack', legend=False)
    hist_fig.suptitle('Histogram of Scores')

    # Create a boxplot of scores by country
    box_fig = plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='Country', y='Score', hue='Name', legend=False)
    box_fig.suptitle('Boxplot of Scores by Country')

    # Return the matplotlib figure
    return hist_fig, box_fig

hist_fig, box_fig = task_func(df)

# Show the figures
plt.show()