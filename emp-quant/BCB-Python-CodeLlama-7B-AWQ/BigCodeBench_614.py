import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(goals, penalties):
    """
    Visualize the distribution of goals and penalties for a number of teams and return the data as a DataFrame with columns 'Team', 'Goals', and 'Penalties'.
    """
    # Create a DataFrame with the given goals and penalties
    df = pd.DataFrame({'Team': goals.keys(), 'Goals': goals.values(), 'Penalties': penalties.values()})

    # Create a pairplot visualization of the goals and penalties distribution for the teams
    sns.pairplot(df, x_vars=['Goals', 'Penalties'], y_vars=['Team'], kind='scatter')

    # Return the DataFrame and the pairplot visualization
    return df, sns.pairplot(df, x_vars=['Goals', 'Penalties'], y_vars=['Team'], kind='scatter')
goals = {'Team A': 10, 'Team B': 5, 'Team C': 8, 'Team D': 12}
penalties = {'Team A': 2, 'Team B': 1, 'Team C': 3, 'Team D': 4}