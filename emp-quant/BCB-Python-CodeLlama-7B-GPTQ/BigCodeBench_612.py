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
        goals = goals[goals['Team'] == team]['Goals'].sum()
        penalties = penalties[penalties['Team'] == team]['Penalties'].sum()

        # Calculate Penalties Cost
        penalties_cost = choice(penalties_costs) * penalties

        # Calculate Performance Score
        performance_score = goals - penalties

        # Append data to DataFrame
        df = df.append({'Team': team, 'Goals': goals, 'Penalties': penalties, 'Penalties Cost': penalties_cost, 'Performance Score': performance_score}, ignore_index=True)

    return df
goals = pd.DataFrame({'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'], 'Goals': [10, 20, 30, 40, 50]})
penalties = pd.DataFrame({'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'], 'Penalties': [5, 10, 15, 20, 25]})