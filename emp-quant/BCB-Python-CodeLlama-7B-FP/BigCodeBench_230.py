import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
COLUMNS = ['Name', 'Age', 'Country', 'Score']
def task_func(df):
    """
    Generates a histogram of scores and a boxplot of scores by country from a pandas DataFrame.
    It considers only unique names for both plots.
    """
    # Check if input is a valid DataFrame
    if not isinstance(df, pd.DataFrame):
        return "Invalid input"
    # Check if required columns are present
    if not all(column in df.columns for column in COLUMNS):
        return "Invalid input"
    # Create a histogram of scores
    sns.histplot(data=df, x="Score", hue="Name", multiple="stack", element="step")
    # Create a boxplot of scores by country
    sns.boxplot(data=df, x="Country", y="Score", hue="Name")
    # Create a figure with both plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.set_title("Histogram of Scores")
    ax2.set_title("Boxplot of Scores by Country")
    fig.tight_layout()
    return fig