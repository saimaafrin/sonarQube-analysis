import numpy as np
import pandas as pd
def task_func(num_teams=5, num_games=100):
    """
    Generate random scores for each team in each game.

    Parameters
    ----------
    num_teams : int, optional
        Number of teams.
    num_games : int, optional
        Number of games.

    Returns
    -------
    DataFrame
        Generated DataFrame containing random scores for each team in each game.
    """
    # Generate random scores for each game
    scores = np.random.randint(0, 100, size=(num_teams, num_games))

    # Create a DataFrame with index=teams, columns=games
    df = pd.DataFrame(scores, index=range(num_teams), columns=range(num_games))

    # Add a column for the total score for each team
    df['total_score'] = df.sum(axis=1)

    return df
num_teams = 5
num_games = 100