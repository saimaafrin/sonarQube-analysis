import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
COLUMNS = ['Name', 'Age', 'Country', 'Score']
def task_func(df):
    """
    Generates a histogram of scores and a boxplot of scores by country from a pandas DataFrame. 
    It considers only unique names for both plots.

    Parameters:
    df (DataFrame): A pandas DataFrame containing the columns 'Name', 'Age', 'Country', and 'Score'.

    Returns:
    matplotlib.figure.Figure: A matplotlib figure containing the histogram and boxplot.

    Requirements:
    - matplotlib.pyplot
    - seaborn
    - pandas

    Note:
    - The function would return "Invalid input" string if the input is invalid (e.g., does not contain the required 'Name' key).
    - The histogram of scores has a title "Histogram of Scores".
    - The boxplot of scores has a title "Boxplot of Scores by Country".

    Example:
    >>> data = pd.DataFrame([{'Name': 'James', 'Age': 30, 'Country': 'USA', 'Score': 85}, {'Name': 'Nick', 'Age': 50, 'Country': 'Australia', 'Score': 80}])
    >>> fig = task_func(data)
    >>> axes = fig.get_axes()
    >>> print(axes[0].get_title())
    Histogram of Scores

    >>> print(task_func("not a dataframe"))
    Invalid input
    """
    if not isinstance(df, pd.DataFrame):
        return "Invalid input"
    if not all(col in df.columns for col in COLUMNS):
        return "Invalid input"
    if not all(df[col].dtype == str for col in COLUMNS):
        return "Invalid input"
    if not all(df[col].dtype == int or df[col].dtype == float for col in ['Age', 'Score']):
        return "Invalid input"
    if not all(df['Name'].is_unique):
        return "Invalid input"

    fig = plt.figure()
    sns.histplot(data=df, x='Score', kde=True, stat='density', color='#0072B2')
    sns.boxplot(data=df, x='Country', y='Score', color='#0072B2')
    plt.title("Histogram of Scores")
    plt.title("Boxplot of Scores by Country")
    return fig