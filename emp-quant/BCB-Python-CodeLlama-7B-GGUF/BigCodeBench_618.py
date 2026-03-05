
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars
def task_func(goals, penalties):
    # Generate random goals and penalties for each team
    goals = [randint(0, 10) for _ in range(len(TEAMS))]
    penalties = [randint(0, 10) for _ in range(len(TEAMS))]
    # Convert penalties to fines
    fines = [penalty * PENALTY_COST for penalty in penalties]
    # Create a DataFrame with match results
    df = pd.DataFrame({'Team': TEAMS, 'Goals': goals, 'Penalties': penalties, 'Fines': fines})
    # Visualize the results
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    sns.barplot(x='Team', y='Goals', data=df, ax=ax1)
    sns.barplot(x='Team', y='Penalties', data=df, ax=ax2)
    return df, [ax1, ax2]