from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties):
    """
    Generates a DataFrame of football match results and plots for goals and penalty costs.

    Parameters:
    goals (int): Number of goals to generate.
    penalties (int): Number of penalties to generate.

    Returns:
    pd.DataFrame: A dataframe containing match results.
    list: A list containing two seaborn plot objects (Axes) for goals and penalty costs.
    """
    # Generate match results
    data = {
        'Team': [TEAMS[randint(0, len(TEAMS) - 1)] for _ in range(goals)],
        'Goals': [randint(0, 10) for _ in range(goals)],
        'Penalty Cost': [randint(0, 10) * PENALTY_COST for _ in range(penalties)]
    }
    df = pd.DataFrame(data)

    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.barplot(x='Team', y='Goals', data=df, ax=axes[0])
    axes[0].set_title('Goals per Team')
    sns.barplot(x='Team', y='Penalty Cost', data=df, ax=axes[1])
    axes[1].set_title('Penalty Costs per Team')

    return df, axes.tolist()