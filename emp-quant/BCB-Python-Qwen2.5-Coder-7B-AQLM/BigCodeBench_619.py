
from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, rng_seed=None):
    if rng_seed is not None:
        seed(rng_seed)
    
    # Simulate match results
    match_results = []
    for _ in range(goals):
        team = TEAMS[randint(0, len(TEAMS) - 1)]
        match_results.append({'Team': team, 'Goals': 1, 'Penalty Cost': PENALTY_COST})
    
    for _ in range(penalties):
        team = TEAMS[randint(0, len(TEAMS) - 1)]
        match_results.append({'Team': team, 'Goals': 0, 'Penalty Cost': PENALTY_COST})
    
    # Create DataFrame
    df = pd.DataFrame(match_results)
    
    # Train Linear Regression model
    X = df[['Goals']]
    y = df['Penalty Cost']
    model = LinearRegression()
    model.fit(X, y)
    
    return df, model