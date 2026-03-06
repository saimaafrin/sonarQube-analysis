
from random import choice
import numpy as np
import pandas as pd

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]

def task_func(goals, penalties, teams=TEAMS, penalties_costs=PENALTIES_COSTS):
    # Create a dictionary to store the performance data for each team
    performance_data = {}

    # Loop through each team and calculate the performance score
    for team in teams:
        # Calculate the goals and penalties for the current team
        goals_for_team = goals[goals['Team'] == team]['Goals'].sum()
        penalties_for_team = penalties[penalties['Team'] == team]['Penalties'].sum()

        # Calculate the penalties cost for the current team
        penalties_cost_for_team = choice(penalties_costs) * penalties_for_team

        # Calculate the performance score for the current team
        performance_score_for_team = goals_for_team - penalties_cost_for_team

        # Add the performance data for the current team to the dictionary
        performance_data[team] = [goals_for_team, penalties_for_team, penalties_cost_for_team, performance_score_for_team]

    # Create a DataFrame from the performance data dictionary
    performance_df = pd.DataFrame.from_dict(performance_data, orient='index')

    # Rename the columns of the DataFrame
    performance_df.columns = ['Goals', 'Penalties', 'Penalties Cost', 'Performance Score']

    return performance_df

performance_df = task_func(goals, penalties)
print(performance_df)