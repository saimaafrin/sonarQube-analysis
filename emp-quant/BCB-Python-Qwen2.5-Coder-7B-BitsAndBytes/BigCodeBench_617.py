
from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
import re

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, rng_seed=None, teams=TEAMS):
    if rng_seed is not None:
        seed(rng_seed)
    
    # Generate random goals and penalties for each team
    team_goals = {team: randint(0, goals) for team in teams}
    team_penalties = {team: randint(0, penalties) for team in teams}
    
    # Calculate total penalty cost
    total_penalty_cost = sum(team_penalties.values()) * PENALTY_COST
    
    # Create DataFrame
    df = pd.DataFrame({
        'Team': list(team_goals.keys()),
        'Goals': list(team_goals.values()),
        'Penalty Cost': [team_penalties[team] * PENALTY_COST for team in teams]
    })
    
    return df

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df['Team'], df['Goals'], color='blue')
plt.xlabel('Teams')
plt.ylabel('Goals Scored')
plt.title('Football Match Goals by Team')
plt.show()