
import pandas as pd
import seaborn as sns

def task_func(goals, penalties):
    # Create a DataFrame with columns 'Team', 'Goals', and 'Penalties'
    df = pd.DataFrame({'Team': goals.keys(), 'Goals': goals.values(), 'Penalties': penalties.values()})

    # Create a pairplot visualization of goals and penalties distribution for the teams
    sns.pairplot(df, x_vars=['Goals', 'Penalties'], y_vars=['Team'], kind='scatter')

    return df, sns.pairplot