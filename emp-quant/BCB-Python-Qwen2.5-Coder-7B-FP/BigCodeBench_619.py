from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties, rng_seed=None):
    """
    Simulates football match results with random goals and penalties for multiple teams,
    and trains a linear regression model to predict penalty costs from goals.

    Parameters:
    goals (int): Number of goals scored in the match.
    penalties (int): Number of penalties awarded in the match.
    rng_seed (int, optional): Seed for the random number generator for reproducibility.

    Returns:
    tuple:
        pd.DataFrame: Contains 'Team', 'Goals', and 'Penalty Cost' columns.
        LinearRegression: Trained model to predict 'Penalty Cost' based on 'Goals'.
    """
    if rng_seed is not None:
        seed(rng_seed)

    # Simulate match results
    team_data = {team: {'Goals': randint(0, goals), 'Penalty Cost': randint(0, penalties * PENALTY_COST)} for team in TEAMS}
    df = pd.DataFrame(list(team_data.values()), index=team_data.keys())

    # Prepare data for linear regression
    X = df[['Goals']]
    y = df['Penalty Cost']

    # Train linear regression model
    model = LinearRegression()
    model.fit(X, y)

    return df, model