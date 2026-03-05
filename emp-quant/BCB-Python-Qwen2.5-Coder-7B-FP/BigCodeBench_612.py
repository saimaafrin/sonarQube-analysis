from random import choice
import numpy as np
import pandas as pd
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]
def task_func(goals, penalties, teams=TEAMS, penalties_costs=PENALTIES_COSTS):
    """
    Generates a performance report DataFrame for teams, detailing goals and penalties.
    
    Parameters:
    - goals (list of int): List of goal counts for each team.
    - penalties (list of int): List of penalty counts for each team.
    - teams (list of str): List of team names.
    - penalties_costs (list of int): List of penalty costs.
    
    Returns:
    - pd.DataFrame: DataFrame with columns 'Team', 'Goals', 'Penalties', 'Penalties Cost', and 'Performance Score'.
    """
    # Ensure the input lists are of the same length
    if len(goals) != len(penalties) or len(goals) != len(teams):
        raise ValueError("The length of goals, penalties, and teams must be the same.")
    
    # Initialize an empty list to store the data for the DataFrame
    data = []
    
    # Iterate over each team and calculate the required values
    for team, goal, penalty in zip(teams, goals, penalties):
        penalty_cost = choice(penalties_costs)  # Randomly select a penalty cost
        performance_score = max(0, goal - penalty)  # Calculate the performance score
        data.append([team, goal, penalty, penalty_cost, performance_score])
    
    # Create the DataFrame
    df = pd.DataFrame(data, columns=['Team', 'Goals', 'Penalties', 'Penalties Cost', 'Performance Score'])
    
    return df
goals = [10, 15, 20, 25, 30]
penalties = [2, 3, 1, 4, 2]