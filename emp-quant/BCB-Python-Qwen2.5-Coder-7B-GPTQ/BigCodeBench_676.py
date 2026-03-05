import pandas as pd
import random
def task_func(df):
    """
    Adds a 'winner' column to the DataFrame based on the scores of the two teams in each match.
    If the scores are equal, the winner is randomly decided.
    
    Parameters:
    df (pandas.DataFrame): A DataFrame with columns 'team1', 'score1', 'team2', 'score2'.
    
    Returns:
    df (pandas.DataFrame): The DataFrame with an additional 'winner' column.
    """
    # Create a new column 'winner' and initialize it with None
    df['winner'] = None
    
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Compare the scores of the two teams
        if row['score1'] > row['score2']:
            df.at[index, 'winner'] = row['team1']
        elif row['score1'] < row['score2']:
            df.at[index, 'winner'] = row['team2']
        else:
            # If scores are equal, randomly choose a winner
            df.at[index, 'winner'] = random.choice([row['team1'], row['team2']])
    
    return df