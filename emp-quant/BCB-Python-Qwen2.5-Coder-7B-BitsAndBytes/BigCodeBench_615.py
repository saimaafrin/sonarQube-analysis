
from random import randint, seed
import pandas as pd

# Method
def task_func(goals, penalties, rng_seed=None):
    if rng_seed is not None:
        seed(rng_seed)
    
    # Define penalty cost
    penalty_cost = 10
    
    # Initialize data structure
    teams = list(goals.keys())
    match_results = []
    
    # Simulate matches
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            team_a_goals = goals[teams[i]] + randint(-2, 3)  # Randomly adjust goals
            team_b_goals = goals[teams[j]] + randint(-2, 3)  # Randomly adjust goals
            
            # Calculate total goals
            total_goals = team_a_goals + team_b_goals
            
            # Determine match result
            if team_a_goals > team_b_goals:
                result = f"{teams[i]} {team_a_goals} - {team_b_goals} {teams[j]}"
                fine = team_b_goals * penalty_cost
            elif team_b_goals > team_a_goals:
                result = f"{teams[j]} {team_b_goals} - {team_a_goals} {teams[i]}"
                fine = team_a_goals * penalty_cost
            else:
                result = f"{teams[i]} {team_a_goals} - {team_b_goals} {teams[j]} (Draw)"
                fine = 0
            
            # Accumulate fines
            goals[teams[i]] += team_a_goals
            goals[teams[j]] += team_b_goals
            penalties[teams[i]] += team_a_goals * penalty_cost
            penalties[teams[j]] += team_b_goals * penalty_cost
            
            match_results.append((result, fine))
    
    # Create DataFrame
    df = pd.DataFrame(match_results, columns=['Match Result', 'Fine'])
    
    return df