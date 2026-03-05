
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
    results = []
    for _ in range(goals):
        team = TEAMS[randint(0, len(TEAMS) - 1)]
        result = {
            'Team': team,
            'Goals': 1,
            'Penalty Cost': PENALTY_COST * penalties
        }
        results.append(result)
    
    # Create DataFrame
    df = pd.DataFrame(results)
    
    # Train Linear Regression model
    X = df[['Goals']]
    y = df['Penalty Cost']
    model = LinearRegression()
    model.fit(X, y)
    
    return df, model