
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Constants
COLUMNS = ['Name', 'Age', 'Country', 'Score']
def task_func(df):
    # Check if input is a valid DataFrame
    if not isinstance(df, pd.DataFrame):
        return "Invalid input"
    
    # Extract unique names for both plots
    names = df['Name'].unique()
    
    # Create histogram of scores
    fig, ax = plt.subplots()
    sns.histplot(data=df, x='Score', hue='Name', multiple='dodge', ax=ax)
    ax.set_title('Histogram of Scores')
    
    # Create boxplot of scores by country
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='Country', y='Score', hue='Name', ax=ax)
    ax.set_title('Boxplot of Scores by Country')
    
    # Return the matplotlib figure
    return fig