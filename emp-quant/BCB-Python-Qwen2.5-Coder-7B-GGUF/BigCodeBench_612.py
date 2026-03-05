
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
    penalties_costs (list): List of penalty costs.
    
    Returns:
    pd.DataFrame: DataFrame with columns 'Team', 'Goals', 'Penalties', 'Penalties Cost', and 'Performance Score'.
    """
    # Ensure the input lists are of the same length
    if len(goals) != len(penalties) or len(goals) != len(teams) or len(goals) != len(penalties_costs):
        raise ValueError("All input lists must be of the same length.")
    
    # Create a DataFrame
    data = {
        'Team': teams,
        'Goals': goals,
        'Penalties': penalties,
        'Penalties Cost': [choice(penalties_costs) for _ in range(len(teams))],
        'Performance Score': [max(0, goal - penalty) for goal, penalty in zip(goals, penalties)]
    }
    df = pd.DataFrame(data)
    
    return df