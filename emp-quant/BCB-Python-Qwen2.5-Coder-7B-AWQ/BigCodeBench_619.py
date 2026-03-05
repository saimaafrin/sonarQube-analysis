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
    goals (int): Number of goals scored by the team.
    penalties (int): Number of penalties taken by the team.
    rng_seed (int, optional): Seed for the random number generator.

    Returns:
    tuple:
    pd.DataFrame: Contains 'Team', 'Goals', and 'Penalty Cost' columns.
    LinearRegression: Trained model to predict 'Penalty Cost' based on 'Goals'.
    """
    if rng_seed is not None:
        seed(rng_seed)

    # Simulate match results
    team_data = []
    for team in TEAMS:
        team_goals = randint(0, goals)
        team_penalties = randint(0, penalties)
        team_data.append({
            'Team': team,
            'Goals': team_goals,
            'Penalty Cost': team_penalties * PENALTY_COST
        })

    # Create DataFrame
    df = pd.DataFrame(team_data)

    # Train Linear Regression model
    X = df[['Goals']]
    y = df['Penalty Cost']
    model = LinearRegression()
    model.fit(X, y)

    return df, model