from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties, rng_seed=None):
    """
    Simulates football match results with random goals and penalties for multiple teams, and trains a linear regression model to predict penalty costs from goals.
    The function should output with:
        tuple:
        pd.DataFrame: Contains 'Team', 'Goals', and 'Penalty Cost' columns.
        LinearRegression: Trained model to predict 'Penalty Cost' based on 'Goals'.
    """
    # Set random seed if provided
    if rng_seed is not None:
        seed(rng_seed)

    # Initialize data frame
    data = pd.DataFrame(columns=['Team', 'Goals', 'Penalty Cost'])

    # Simulate match results
    for team in TEAMS:
        # Generate random goals and penalties
        goals = randint(0, 10)
        penalties = randint(0, 10)

        # Add data to data frame
        data = data.append({'Team': team, 'Goals': goals, 'Penalty Cost': penalties * PENALTY_COST}, ignore_index=True)

    # Train linear regression model
    X = data['Goals']
    y = data['Penalty Cost']
    model = LinearRegression().fit(X, y)

    # Return data frame and trained model
    return data, model