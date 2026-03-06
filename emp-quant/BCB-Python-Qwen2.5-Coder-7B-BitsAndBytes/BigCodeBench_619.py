
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
    data = {
        'Team': [],
        'Goals': [],
        'Penalty Cost': []
    }
    
    for _ in range(goals + penalties):
        team = TEAMS[randint(0, len(TEAMS) - 1)]
        goal_or_penalty = randint(0, 1)  # 0 for goal, 1 for penalty
        
        if goal_or_penalty == 0:
            data['Team'].append(team)
            data['Goals'].append(1)
            data['Penalty Cost'].append(0)
        else:
            data['Team'].append(team)
            data['Goals'].append(0)
            data['Penalty Cost'].append(PENALTY_COST)
    
    df = pd.DataFrame(data)
    
    # Train linear regression model
    X = df[['Goals']]
    y = df['Penalty Cost']
    model = LinearRegression()
    model.fit(X, y)
    
    return df, model