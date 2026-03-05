
from random import randint, seed
import pandas as pd

# Method
def task_func(goals, penalties, rng_seed=None):
    if rng_seed is not None:
        seed(rng_seed)
    
    # Define the cost of penalties in fines
    penalty_cost = 100
    
    # Initialize a dictionary to store team results
    team_results = {}
    
    # Simulate the matches for each team
    for team in goals:
        # Calculate the total goals for the team
        total_goals = goals[team]
        
        # Calculate the total fines for the team based on penalties
        total_fines = penalties[team] * penalty_cost
        
        # Store the results in the dictionary
        team_results[team] = {'Goals': total_goals, 'Fines': total_fines}
    
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(list(team_results.items()), columns=['Team', 'Match Result'])
    
    return df

penalties = {
    'Team A': 1,
    'Team B': 2,
    'Team C': 0
}

result_df = task_func(goals, penalties, rng_seed=42)
print(result_df)