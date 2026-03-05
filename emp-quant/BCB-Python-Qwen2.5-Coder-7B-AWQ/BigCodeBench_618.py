from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties):
    """
    Generate and visualize a Pandas DataFrame of the results of football matches for multiple teams 'Team' with random goals 'Goals' and penalties 'Penalty Cost'.
    Penalties are converted into fines according to penalty costs.
    
    Parameters:
    goals (int): Number of goals to simulate.
    penalties (int): Number of penalties to simulate.
    
    Returns:
    pd.DataFrame: A dataframe containing match results.
    list: A list containing two seaborn plot objects (Axes) for goals and penalty costs.
    """
    # Simulate match results
    data = {
        'Team': [TEAMS[randint(0, len(TEAMS) - 1)] for _ in range(goals)],
        'Goals': [randint(0, 10) for _ in range(goals)],
        'Penalty Cost': [randint(0, 10) * PENALTY_COST for _ in range(penalties)]
    }
    df = pd.DataFrame(data)
    
    # Convert penalties to fines
    df['Fine'] = df['Penalty Cost']
    
    # Create plots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.barplot(x='Team', y='Goals', data=df, ax=axes[0])
    axes[0].set_title('Goals by Team')
    
    sns.barplot(x='Team', y='Fine', data=df, ax=axes[1])
    axes[1].set_title('Fines by Team')
    
    return df, axes.tolist()