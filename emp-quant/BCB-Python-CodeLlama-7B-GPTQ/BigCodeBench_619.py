from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties, rng_seed=None):
    """Simulates football match results with random goals and penalties for multiple teams, and trains a linear regression model to predict penalty costs from goals.

    Args:
        goals (int): Number of goals scored in the match.
        penalties (int): Number of penalties awarded in the match.
        rng_seed (int, optional): Random seed for reproducibility. Defaults to None.

    Returns:
        tuple:
            pd.DataFrame: Contains 'Team', 'Goals', and 'Penalty Cost' columns.
            LinearRegression: Trained model to predict 'Penalty Cost' based on 'Goals'.
    """
    # Set random seed for reproducibility
    if rng_seed is not None:
        seed(rng_seed)

    # Generate random goals and penalties for each team
    team_goals = {team: randint(0, 10) for team in TEAMS}
    team_penalties = {team: randint(0, 2) for team in TEAMS}

    # Calculate total goals and penalties for each team
    team_totals = {team: team_goals[team] + team_penalties[team] for team in TEAMS}

    # Create DataFrame with team, goals, and penalty cost columns
    df = pd.DataFrame(
        {
            "Team": TEAMS,
            "Goals": [team_goals[team] for team in TEAMS],
            "Penalty Cost": [team_penalties[team] * PENALTY_COST for team in TEAMS],
        }
    )

    # Train linear regression model to predict penalty cost from goals
    X = df["Goals"]
    y = df["Penalty Cost"]
    model = LinearRegression().fit(X, y)

    return df, model