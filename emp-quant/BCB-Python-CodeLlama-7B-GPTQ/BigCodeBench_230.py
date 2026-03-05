import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def task_func(df):
    """
    Generates a histogram of scores and a boxplot of scores by country from a pandas DataFrame.
    It considers only unique names for both plots.
    """
    # Check if the input is a valid pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        return "Invalid input"

    # Extract the unique names from the DataFrame
    names = df['Name'].unique()

    # Create a histogram of scores
    fig, ax = plt.subplots()
    ax.hist(df['Score'], bins=20, alpha=0.5, label='Histogram of Scores')
    ax.set_title('Histogram of Scores')
    ax.set_xlabel('Score')
    ax.set_ylabel('Frequency')

    # Create a boxplot of scores by country
    sns.boxplot(x='Country', y='Score', data=df, ax=ax)
    ax.set_title('Boxplot of Scores by Country')
    ax.set_xlabel('Country')
    ax.set_ylabel('Score')

    # Return the matplotlib figure
    return fig
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35, 25, 30, 35],
    'Country': ['USA', 'Canada', 'Mexico', 'USA', 'Canada', 'Mexico'],
    'Score': [85, 70, 65, 90, 80, 75]
})