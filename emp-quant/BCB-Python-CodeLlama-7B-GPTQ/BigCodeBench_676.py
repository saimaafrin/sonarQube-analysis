import pandas as pd
import random
def task_func(df):
    """
    Generate a DataFrame that contains savegames for a number of games between different teams. Each row of the input DataFrame represents a match, and contains two teams and their respective scores. The function adds a 'winner' column to the DataFrame, which is the team with the highest score in each match. If the scores are equal, the winner is should be randomly decided.
    """
    # Add a 'winner' column to the DataFrame
    df['winner'] = ''

    # Iterate over each row of the DataFrame
    for index, row in df.iterrows():
        # If the scores are equal, randomly decide the winner
        if row['score1'] == row['score2']:
            df.at[index, 'winner'] = random.choice([row['team1'], row['team2']])
        # Otherwise, set the winner to the team with the higher score
        else:
            df.at[index, 'winner'] = row['team1'] if row['score1'] > row['score2'] else row['team2']

    return df
df = pd.DataFrame({'team1': ['Team A', 'Team B', 'Team C'],
                   'team2': ['Team D', 'Team E', 'Team F'],
                   'score1': [10, 20, 30],
                   'score2': [20, 30, 40]})