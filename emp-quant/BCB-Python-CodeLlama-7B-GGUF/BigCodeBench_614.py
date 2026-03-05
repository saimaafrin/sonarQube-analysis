
import pandas as pd
import seaborn as sns

def task_func(goals, penalties):
    # Create a DataFrame with the goals and penalties for each team
    df = pd.DataFrame({'Team': goals.keys(), 'Goals': goals.values(), 'Penalties': penalties.values()})
    
    # Visualize the distribution of goals and penalties for each team
    sns.pairplot(df, x_vars=['Goals', 'Penalties'], y_vars=['Team'], kind='scatter')
    
    return df, sns.pairplot