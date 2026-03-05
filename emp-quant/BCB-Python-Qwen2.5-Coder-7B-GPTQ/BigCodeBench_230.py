import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
COLUMNS = ['Name', 'Age', 'Country', 'Score']
def task_func(df):
    # Check if the input is a DataFrame and contains the required columns
    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in COLUMNS):
        return "Invalid input"
    
    # Filter out duplicate names
    df = df.drop_duplicates(subset='Name')
    
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Histogram of scores
    sns.histplot(data=df, x='Score', ax=axes[0], kde=True)
    axes[0].set_title('Histogram of Scores')
    
    # Boxplot of scores by country
    sns.boxplot(data=df, x='Country', y='Score', ax=axes[1])
    axes[1].set_title('Boxplot of Scores by Country')
    
    # Adjust layout
    plt.tight_layout()
    
    return fig