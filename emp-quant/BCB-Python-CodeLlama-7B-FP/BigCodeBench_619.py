from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties, rng_seed=None):
    """
    Simulates football match results with random goals and penalties for multiple teams, and trains a linear regression model to predict penalty costs from goals.
    """
    # Set random seed for reproducibility
    if rng_seed is not None:
        seed(rng_seed)
    # Generate random goals and penalties for each team
    results = []
    for team in TEAMS:
        goals = randint(0, 10)
        penalties = randint(0, 10)
        results.append((team, goals, penalties))
    # Create a DataFrame with the results
    df = pd.DataFrame(results, columns=['Team', 'Goals', 'Penalties'])
    # Add penalty cost column to DataFrame
    df['Penalty Cost'] = df['Goals'] * PENALTY_COST
    # Train a linear regression model to predict penalty costs from goals
    X = df[['Goals']]
    y = df['Penalty Cost']
    model = LinearRegression().fit(X, y)
    # Return the DataFrame and the trained model
    return df, model