import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
COLUMNS = ['Name', 'Age', 'Country', 'Score']
def task_func(df):
    """
    Generates a histogram of scores and a boxplot of scores by country from a pandas DataFrame.
    It considers only unique names for both plots.
    """
    # Check if the input is a valid DataFrame
    if not isinstance(df, pd.DataFrame):
        return "Invalid input"

    # Check if the DataFrame has the required columns
    if not set(COLUMNS).issubset(df.columns):
        return "Invalid input"

    # Create a histogram of scores
    sns.histplot(data=df, x="Score", hue="Country", multiple="dodge",
                  element="step", fill=True, palette="Set2")
    plt.title("Histogram of Scores")

    # Create a boxplot of scores by country
    sns.boxplot(data=df, x="Country", y="Score", hue="Country",
                 palette="Set2", fliersize=0.5, linewidth=2)
    plt.title("Boxplot of Scores by Country")

    # Return the matplotlib figure
    return plt.gcf()
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35, 25, 30, 35],
    "Country": ["USA", "Canada", "Mexico", "USA", "Canada", "Mexico"],
    "Score": [80, 70, 60, 80, 70, 60]
})