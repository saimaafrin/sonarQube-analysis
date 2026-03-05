
from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, rng_seed=None):
    # Seed the random number generator
    if rng_seed is not None:
        seed(rng_seed)

    # Simulate football match results
    results = []
    for _ in range(goals):
        team = TEAMS[randint(0, len(TEAMS) - 1)]
        goals_scored = randint(0, 10)
        penalty = 'Yes' if randint(0, 1) == 1 else 'No'
        results.append((team, goals_scored, penalty))

    # Convert results to DataFrame
    df = pd.DataFrame(results, columns=['Team', 'Goals', 'Penalty'])

    # Filter results to include only those with penalties
    df_penalties = df[df['Penalty'] == 'Yes']

    # Train a linear regression model to predict penalty costs
    X = df_penalties['Goals'].values.reshape(-1, 1)
    y = df_penalties['Penalty'].apply(lambda x: PENALTY_COST).values
    model = LinearRegression()
    model.fit(X, y)

    return df, model