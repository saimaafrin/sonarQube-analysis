
from random import choice
import numpy as np
import pandas as pd
# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]
def task_func(goals, penalties, teams=TEAMS, penalties_costs=PENALTIES_COSTS):
    # Calculate goals and penalties
    goals_df = goals.groupby('Team').sum()
    penalties_df = penalties.groupby('Team').sum()
    # Calculate penalties cost
    penalties_cost_df = penalties_df.apply(lambda x: choice(penalties_costs, x))
    # Calculate performance score
    performance_score_df = goals_df - penalties_cost_df
    # Create DataFrame
    df = pd.DataFrame({
        'Team': goals_df.index,
        'Goals': goals_df['Goals'],
        'Penalties': penalties_df['Penalties'],
        'Penalties Cost': penalties_cost_df['Penalties Cost'],
        'Performance Score': performance_score_df['Performance Score']
    })
    return df