from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties, rng_seed=None):
    if rng_seed is not None:
        seed(rng_seed)
    
    # Simulate match results
    data = {
        'Team': TEAMS,
        'Goals': [randint(0, goals) for _ in TEAMS],
        'Penalty Cost': [randint(0, penalties) * PENALTY_COST for _ in TEAMS]
    }
    df = pd.DataFrame(data)
    
    # Train linear regression model
    X = df[['Goals']]
    y = df['Penalty Cost']
    model = LinearRegression()
    model.fit(X, y)
    
    return df, model