import pandas as pd
import seaborn as sns
def task_func(goals, penalties):
    # Create a DataFrame with the goals and penalties for each team
    df = pd.DataFrame({'Team': goals.keys(),
                       'Goals': goals.values(),
                       'Penalties': penalties.values()})

    # Visualize the distribution of goals and penalties for each team
    sns.pairplot(df, x_vars=['Goals', 'Penalties'], y_vars=['Team'])

    # Return the DataFrame and the pairplot
    return df, sns.pairplot(df, x_vars=['Goals', 'Penalties'], y_vars=['Team'])
goals = {'Team A': 10, 'Team B': 5, 'Team C': 8}
penalties = {'Team A': 2, 'Team B': 1, 'Team C': 3}