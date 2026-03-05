
import pandas as pd
import seaborn as sns
import numpy as np

def task_func(goals, penalties):
    # Create a DataFrame with the teams, goals, and penalties
    teams = np.arange(1, len(goals) + 1)
    data = {'Team': teams, 'Goals': goals, 'Penalties': penalties}
    df = pd.DataFrame(data)
    
    # Create a seaborn pairplot to visualize the distribution of goals and penalties
    pairplot = sns.pairplot(df, x_vars=['Goals'], y_vars=['Penalties'], kind='scatter')
    
    return df, pairplot