
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(goals, penalties):
    # Create a DataFrame with the goals and penalties for the teams
    data = {
        'Team': range(1, len(goals) + 1),
        'Goals': goals,
        'Penalties': penalties
    }
    df = pd.DataFrame(data)
    
    # Create a seaborn pairplot visualization of goals and penalties distribution for the teams
    pairplot = sns.pairplot(df, vars=['Goals', 'Penalties'], kind='reg')
    
    # Return the DataFrame and the Axes object
    return df, pairplot.axes