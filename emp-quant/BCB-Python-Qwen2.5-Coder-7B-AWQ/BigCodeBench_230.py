import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
COLUMNS = ['Name', 'Age', 'Country', 'Score']
def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        return "Invalid input"
    
    # Check if the DataFrame contains the required columns
    if not all(col in df.columns for col in COLUMNS):
        return "Invalid input"
    
    # Remove duplicates based on 'Name'
    df = df.drop_duplicates(subset='Name')
    
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Histogram of scores
    sns.histplot(df['Score'], ax=axes[0], kde=True)
    axes[0].set_title("Histogram of Scores")
    
    # Boxplot of scores by country
    sns.boxplot(x='Country', y='Score', data=df, ax=axes[1])
    axes[1].set_title("Boxplot of Scores by Country")
    
    # Adjust layout
    plt.tight_layout()
    
    return fig