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
    # Create a DataFrame
    data = {
        'Team': range(1, len(goals) + 1),
        'Goals': goals,
        'Penalties': penalties
    }
    df = pd.DataFrame(data)
    
    # Create a pairplot visualization
    pairplot = sns.pairplot(df, x_vars=['Goals'], y_vars=['Penalties'], kind='reg')
    
    # Return the DataFrame and the Axes object
    return df, pairplot.axes
goals = [10, 15, 20, 25, 30]
penalties = [2, 4, 6, 8, 10]