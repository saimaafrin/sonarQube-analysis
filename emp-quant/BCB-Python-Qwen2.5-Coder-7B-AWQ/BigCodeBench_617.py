from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
import re
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties, rng_seed=None, teams=TEAMS):
    # Seed the random number generator if a seed is provided
    if rng_seed is not None:
        seed(rng_seed)
    
    # Initialize lists to store team names, goals, and penalty costs
    team_names = []
    team_goals = []
    penalty_costs = []
    
    # Generate random goals and penalties for each team
    for team in teams:
        team_goals.append(randint(0, goals))
        penalty_costs.append(randint(0, penalties) * PENALTY_COST)
        team_names.append(team)
    
    # Create a DataFrame from the generated data
    df = pd.DataFrame({
        'Team': team_names,
        'Goals': team_goals,
        'Penalty Cost': penalty_costs
    })
    
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(df['Team'], df['Goals'], color='blue', label='Goals')
    plt.bar(df['Team'], df['Penalty Cost'], color='red', alpha=0.5, label='Penalty Cost')
    plt.xlabel('Teams')
    plt.ylabel('Values')
    plt.title('Football Match Results')
    plt.legend()
    plt.show()
    
    return df