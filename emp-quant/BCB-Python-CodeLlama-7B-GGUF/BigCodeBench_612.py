
from random import choice
import numpy as np
import pandas as pd

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]

def task_func(goals, penalties, teams=TEAMS, penalties_costs=PENALTIES_COSTS):
    # Create a dictionary to store the results
    results = {}

    # Iterate over the teams
    for team in teams:
        # Calculate the number of goals and penalties for the current team
        goals_count = goals[team]
        penalties_count = penalties[team]

        # Calculate the penalties cost for the current team
        penalties_cost = choice(penalties_costs) * penalties_count

        # Calculate the performance score for the current team
        performance_score = goals_count - penalties_cost

        # Add the results to the dictionary
        results[team] = (goals_count, penalties_count, penalties_cost, performance_score)

    # Create a DataFrame from the results dictionary
    df = pd.DataFrame.from_dict(results, orient='index')

    # Rename the columns
    df.columns = ['Goals', 'Penalties', 'Penalties Cost', 'Performance Score']

    return df