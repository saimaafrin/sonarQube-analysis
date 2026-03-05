
from random import choice
import numpy as np
import pandas as pd

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]

def task_func(goals, penalties, teams=TEAMS, penalties_costs=PENALTIES_COSTS):
    # Initialize a list to hold the performance report data
    performance_report = []

    # Iterate over each team
    for team in teams:
        # Get the goal and penalty counts for the team
        goal_count = goals[team]
        penalty_count = penalties[team]

        # Calculate the penalties cost using a random multiplier
        penalties_cost = penalty_count * choice(PENALTIES_COSTS)

        # Calculate the performance score
        performance_score = max(0, goal_count - penalty_count)

        # Append the data to the performance report list
        performance_report.append({
            'Team': team,
            'Goals': goal_count,
            'Penalties': penalty_count,
            'Penalties Cost': penalties_cost,
            'Performance Score': performance_score
        })

    # Convert the performance report list to a DataFrame
    performance_df = pd.DataFrame(performance_report)

    # Return the DataFrame
    return performance_df

penalties = {
    'Team A': 2,
    'Team B': 3,
    'Team C': 1,
    'Team D': 2,
    'Team E': 4
}

performance_report = task_func(goals, penalties)
print(performance_report)