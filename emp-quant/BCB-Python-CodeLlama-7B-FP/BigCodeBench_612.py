from random import choice
import numpy as np
import pandas as pd
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]
def task_func(goals, penalties, teams=TEAMS, penalties_costs=PENALTIES_COSTS):
    """
    Generates a performance report DataFrame for teams, detailing goals and penalties.
    For each team, the function fetches goal and penalty counts, calculates 'Penalties Cost' using a random multiplier from a predefined list, and computes a 'Performance Score' as the non-negative difference between goals and penalties.
    Return a Dataframe with colomns 'Team', 'Goals', 'Penalties', 'Penalties Cost', and 'Performance Score'.
    """
    # Initialize DataFrame
    df = pd.DataFrame(columns=['Team', 'Goals', 'Penalties', 'Penalties Cost', 'Performance Score'])

    # Iterate over teams
    for team in teams:
        # Fetch goal and penalty counts for the current team
        goals_count = goals[team]
        penalties_count = penalties[team]

        # Calculate 'Penalties Cost' using a random multiplier from a predefined list
        penalties_cost = np.random.choice(penalties_costs) * penalties_count

        # Compute 'Performance Score' as the non-negative difference between goals and penalties
        performance_score = goals_count - penalties_count

        # Add row to DataFrame
        df = df.append({'Team': team, 'Goals': goals_count, 'Penalties': penalties_count, 'Penalties Cost': penalties_cost, 'Performance Score': performance_score}, ignore_index=True)

    return df
goals = {'Team A': 10, 'Team B': 20, 'Team C': 30, 'Team D': 40, 'Team E': 50}
penalties = {'Team A': 5, 'Team B': 10, 'Team C': 15, 'Team D': 20, 'Team E': 25}