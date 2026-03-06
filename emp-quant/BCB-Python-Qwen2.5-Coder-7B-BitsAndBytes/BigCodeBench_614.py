
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(goals, penalties):
    """
    Visualize the distribution of goals and penalties for a number of teams and return the data as a DataFrame with columns 'Team', 'Goals' and 'Penalties'.

    Parameters:
    goals (list): A list of goals scored by each team.
    penalties (list): A list of penalties taken by each team.

    Returns:
    tuple: A tuple containing:
        DataFrame: A pandas DataFrame with the goals and penalties for the teams.
        Axes: A seaborn pairplot visualization of goals and penalties distribution for the teams.
    """
    # Create a DataFrame from the goals and penalties lists
    data = {
        'Team': range(1, len(goals) + 1),
        'Goals': goals,
        'Penalties': penalties
    }
    df = pd.DataFrame(data)
    
    # Create a pairplot visualization using seaborn
    pairplot_figure = sns.pairplot(df, vars=['Goals', 'Penalties'])
    
    # Display the plot
    plt.show()
    
    return df, pairplot_figure.axes.flatten()

df, axes = task_func(goals, penalties)
print(df)