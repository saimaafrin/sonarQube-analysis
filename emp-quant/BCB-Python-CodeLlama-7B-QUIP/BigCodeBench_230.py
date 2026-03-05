
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Constants
COLUMNS = ['Name', 'Age', 'Country', 'Score']
def task_func(df):
    if not isinstance(df, pd.DataFrame):
        return "Invalid input"
    # Create a histogram of scores
    scores = df[COLUMNS['Score']].unique()
    fig, ax = plt.subplots()
    ax.hist(scores, bins=50)
    ax.set_xlabel('Score')
    ax.set_ylabel('Count')
    ax.set_title('Histogram of Scores')
    plt.show()
    # Create a boxplot of scores by country
    scores_by_country = df[COLUMNS['Score']].groupby(COLUMNS['Country'])
    fig, ax = plt.subplots()
    ax.boxplot(scores_by_country)
    ax.set_xlabel('Country')
    ax.set_ylabel('Score')
    ax.set_title('Boxplot of Scores by Country')
    plt.show()
    return fig