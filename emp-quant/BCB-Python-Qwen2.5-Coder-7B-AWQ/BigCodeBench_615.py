from random import randint, seed
import pandas as pd
def task_func(goals, penalties, rng_seed=None):
    if rng_seed is not None:
        seed(rng_seed)
    
    # Define the cost of penalties in fines
    penalty_cost = 100
    
    # Initialize a list to store team results
    team_results = []
    
    # Loop through each team and calculate their match result
    for team, (goals_scored, penalties_taken) in goals.items():
        # Calculate total goals and fines
        total_goals = goals_scored
        total_fines = penalties_taken * penalty_cost
        
        # Append the result to the list
        team_results.append({'Team': team, 'Match Result': f'{total_goals} goals, {total_fines} fines'})
    
    # Create a DataFrame from the list of results
    result_df = pd.DataFrame(team_results)
    
    return result_df
goals = {
    'Team A': (2, 1),
    'Team B': (1, 2),
    'Team C': (3, 0)
}
penalties = {
    'Team A': 1,
    'Team B': 2,
    'Team C': 0
}