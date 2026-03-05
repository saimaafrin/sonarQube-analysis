from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
import re
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties, rng_seed=None, teams=TEAMS):
    if rng_seed is not None:
        seed(rng_seed)
    
    # Generate random goals and penalties for each team
    team_data = {team: {'Goals': randint(0, goals), 'Penalties': randint(0, penalties)} for team in teams}
    
    # Convert penalties to penalty costs
    for team in team_data:
        team_data[team]['Penalty Cost'] = team_data[team]['Penalties'] * PENALTY_COST
    
    # Create DataFrame
    df = pd.DataFrame(list(team_data.values()), index=team_data.keys())
    
    # Add original match results
    df['Original Match Result'] = df['Goals'].astype(str) + ' - ' + df['Goals'].astype(str)
    
    return df