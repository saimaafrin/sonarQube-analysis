
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties):
    # Generate a random number of goals for each team
    goals = {team: randint(0, 10) for team in TEAMS}
    # Generate a random number of penalties for each team
    penalties = {team: randint(0, 10) for team in TEAMS}
    # Calculate the total cost of penalties
    total_penalties = sum(penalties.values()) * PENALTY_COST
    # Calculate the total cost of goals
    total_goals = sum(goals.values()) * PENALTY_COST
    # Calculate the profit/loss for each team
    profits = {team: goals[team] - penalties[team] for team in TEAMS}
    # Create a Pandas DataFrame with the results
    df = pd.DataFrame({
        'Team': TEAMS,
        'Goals': goals,
        'Penalties': penalties,
        'Profit': profits
    })
    # Create a Seaborn bar plot for the profit/loss for each team
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=df['Team'], y=df['Profit'], ax=ax)
    # Create a Seaborn bar plot for the number of goals for each team
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=df['Team'], y=df['Goals'], ax=ax)
    # Create a Seaborn bar plot for the number of penalties for each team
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=df['Team'], y=df['Penalties'], ax=ax)
    return df, [ax1, ax2, ax3]