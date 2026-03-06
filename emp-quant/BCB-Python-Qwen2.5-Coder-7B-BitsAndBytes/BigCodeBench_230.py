
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
COLUMNS = ['Name', 'Age', 'Country', 'Score']

def task_func(df):
    # Check if the input is a valid DataFrame
    if not isinstance(df, pd.DataFrame) or COLUMNS[0] not in df.columns:
        return "Invalid input"
    
    # Filter out duplicate names
    df_unique = df.drop_duplicates(subset='Name')
    
    # Create a figure to hold both plots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Histogram of scores
    sns.histplot(data=df_unique, x='Score', ax=axes[0], kde=True)
    axes[0].set_title('Histogram of Scores')
    
    # Boxplot of scores by country
    sns.boxplot(data=df_unique, x='Country', y='Score', ax=axes[1])
    axes[1].set_title('Boxplot of Scores by Country')
    
    # Adjust layout
    plt.tight_layout()
    
    return fig