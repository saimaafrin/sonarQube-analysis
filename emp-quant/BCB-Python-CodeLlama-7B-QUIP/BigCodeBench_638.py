
import numpy as np
import pandas as pd

def task_func(num_teams=5, num_games=100):
    # Generate random scores for each game played by each team
    scores = np.random.randint(100, size=(num_teams, num_games))

    # Create a DataFrame with index=teams, columns=games
    df = pd.DataFrame(scores, index=range(num_teams), columns=range(num_games))

    return df