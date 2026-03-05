from random import randint, seed
import pandas as pd
def task_func(goals, penalties, rng_seed=None):
    if rng_seed is not None:
        seed(rng_seed)
    
    # Define the cost of penalties in fines
    penalty_cost = 100  # Each penalty results in a fine of 100 units
    
    # Initialize a dictionary to store team results
    team_results = {}
    
    # Simulate the matches and calculate goals and fines
    for team, (goals_team, penalties_team) in goals.items():
        total_goals = goals_team
        total_fines = penalties_team * penalty_cost
        
        # Add the results to the dictionary
        team_results[team] = {'Goals': total_goals, 'Fines': total_fines}
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(list(team_results.items()), columns=['Team', 'Match Result'])
    
    return df
goals = {
    'Team A': (randint(0, 10), randint(0, 5)),
    'Team B': (randint(0, 10), randint(0, 5)),
    'Team C': (randint(0, 10), randint(0, 5)),
    'Team D': (randint(0, 10), randint(0, 5)),
    'Team E': (randint(0, 10), randint(0, 5)),
}
penalties = {
    'Team A': randint(0, 5),
    'Team B': randint(0, 5),
    'Team C': randint(0, 5),
    'Team D': randint(0, 5),
    'Team E': randint(0, 5),
}