import numpy as np
import pandas as pd
def task_func(num_teams=5, num_games=100):
    # Create a DataFrame with random scores for each team in each game
    teams = [f'Team {i+1}' for i in range(num_teams)]
    games = [f'Game {i+1}' for i in range(num_games)]
    scores = np.random.randint(0, 101, size=(num_teams, num_games))
    df = pd.DataFrame(scores, index=teams, columns=games)
    return df