
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
COLUMNS = ['Name', 'Age', 'Country', 'Score']

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        return "Invalid input"
    
    # Check if the DataFrame contains the required columns
    if not all(col in df.columns for col in COLUMNS):
        return "Invalid input"
    
    # Remove duplicates based on 'Name'
    df_unique = df.drop_duplicates(subset='Name')
    
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Histogram of Scores
    sns.histplot(df_unique['Score'], ax=axes[0], kde=True)
    axes[0].set_title("Histogram of Scores")
    
    # Boxplot of Scores by Country
    sns.boxplot(x='Country', y='Score', data=df_unique, ax=axes[1])
    axes[1].set_title("Boxplot of Scores by Country")
    
    # Adjust layout
    plt.tight_layout()
    
    return fig