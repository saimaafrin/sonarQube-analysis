
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
    
    # Calculate penalty costs
    team_penalty_costs = {team: team_penalties[team] * PENALTY_COST for team in teams}
    
    # Create DataFrame
    df = pd.DataFrame({
        'Team': list(team_goals.keys()),
        'Goals': list(team_goals.values()),
        'Penalty Cost': list(team_penalty_costs.values())
    })
    
    # Add original match results
    df['Match Result'] = df['Team'].map(lambda team: f"{team} {team_goals[team]} - {team_penalties[team]}")
    
    return df

# Visualization
plt.figure(figsize=(10, 6))
plt.bar(df['Team'], df['Goals'], color='blue')
plt.xlabel('Team')
plt.ylabel('Goals')
plt.title('Goals Scored by Each Team')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(df['Team'], df['Penalty Cost'], color='red')
plt.xlabel('Team')
plt.ylabel('Penalty Cost')
plt.title('Penalty Costs by Each Team')
plt.show()