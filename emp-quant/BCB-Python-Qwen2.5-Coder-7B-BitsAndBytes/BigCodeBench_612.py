
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
    # Ensure inputs match the number of teams
    if len(goals) != len(teams) or len(penalties) != len(teams):
        raise ValueError("Lengths of goals, penalties, and teams must be equal.")
    
    # Initialize an empty list to store data rows
    data = []
    
    # Iterate over each team
    for i in range(len(teams)):
        team = teams[i]
        goal_count = goals[i]
        penalty_count = penalties[i]
        
        # Randomly select a penalties cost
        penalties_cost = choice(penalties_costs)
        
        # Calculate performance score
        performance_score = max(goal_count - penalty_count, 0)
        
        # Append data row to the list
        data.append([team, goal_count, penalty_count, penalties_cost, performance_score])
    
    # Create DataFrame from the collected data
    df = pd.DataFrame(data, columns=['Team', 'Goals', 'Penalties', 'Penalties Cost', 'Performance Score'])
    
    return df