
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
    if not all(column in df.columns for column in COLUMNS):
        return "Invalid input"
    
    # Filter unique names
    df = df[~df['Name'].duplicated(keep='first')]
    
    # Create a figure with a specified size
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Histogram of scores
    sns.histplot(df['Score'], ax=axes[0], kde=True)
    axes[0].set_title('Histogram of Scores')
    
    # Boxplot of scores by country
    sns.boxplot(x=df['Country'], y=df['Score'], ax=axes[1])
    axes[1].set_title('Boxplot of Scores by Country')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return fig