import numpy as np
import pandas as pd
def task_func(num_teams=5, num_games=100):
    # Generate random scores for each game played by each team
    scores = np.random.randint(0, 100, size=(num_teams, num_games))
    
    # Create a DataFrame with teams as index and games as columns
    teams = [f'Team {i+1}' for i in range(num_teams)]
    games = [f'Game {i+1}' for i in range(num_games)]
    df = pd.DataFrame(scores, index=teams, columns=games)
    
    return df