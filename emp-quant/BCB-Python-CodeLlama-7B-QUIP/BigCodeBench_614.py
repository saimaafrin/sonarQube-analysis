
import pandas as pd
import seaborn as sns

def task_func(goals, penalties):
    # Create a DataFrame with the goals and penalties for each team
    df = pd.DataFrame({
        'Team': goals.index,
        'Goals': goals.values,
        'Penalties': penalties.values
    })

    # Visualize the distribution of goals and penalties for each team
    ax = sns.pairplot(df, x_vars=['Goals', 'Penalties'], y_vars=['Goals', 'Penalties'],
                      map=sns.kdeplot)

    return df, ax