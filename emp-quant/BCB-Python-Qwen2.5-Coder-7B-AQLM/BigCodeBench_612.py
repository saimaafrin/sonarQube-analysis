
from random import choice
import numpy as np
import pandas as pd

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]

def task_func(goals, penalties, teams=TEAMS, penalties_costs=PENALTIES_COSTS):
    """
    Generates a performance report DataFrame for teams, detailing goals and penalties.
    
    Parameters:
    goals (list): List of goal counts for each team.
    penalties (list): List of penalty counts for each team.
    teams (list): List of team names.
    penalties_costs (list): List of penalties costs.
    
    Returns:
    pd.DataFrame: DataFrame with columns 'Team', 'Goals', 'Penalties', 'Penalties Cost', and 'Performance Score'.
    """
    # Ensure the lists are of the same length
    if len(goals) != len(penalties) or len(goals) != len(teams) or len(goals) != len(penalties_costs):
        raise ValueError("All input lists must be of the same length.")
    
    # Initialize lists to store the data
    team_data = []
    
    # Iterate over each team and calculate the required values
    for team, goal, penalty in zip(teams, goals, penalties):
        penalty_cost = choice(penalties_costs)
        performance_score = max(0, goal - penalty)
        team_data.append([team, goal, penalty, penalty_cost, performance_score])
    
    # Create the DataFrame
    df = pd.DataFrame(team_data, columns=['Team', 'Goals', 'Penalties', 'Penalties Cost', 'Performance Score'])
    
    return df