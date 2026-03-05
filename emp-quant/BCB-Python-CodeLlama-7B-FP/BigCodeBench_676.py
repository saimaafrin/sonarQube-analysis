import pandas as pd
import random
def task_func(df):
    """
    Generate a DataFrame that contains savegames for a number of games between different teams.
    Each row of the input DataFrame represents a match, and contains two teams and their respective scores.
    The function adds a 'winner' column to the DataFrame, which is the team with the highest score in each match.
    If the scores are equal, the winner is should be randomly decided.
    """
    df['winner'] = df.apply(lambda row: row.iloc[0] if row.iloc[0] > row.iloc[1] else random.choice([row.iloc[0], row.iloc[1]]), axis=1)
    return df
df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [10, 20, 30], 'score2': [20, 30, 40]})