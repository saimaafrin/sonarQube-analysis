import pandas as pd
import random
def task_func(df):
    """
    Adds a 'winner' column to the DataFrame, which is the team with the highest score in each match.
    If the scores are equal, the winner is randomly decided.
    
    Parameters:
    df (pandas.DataFrame): Input DataFrame with columns 'team1', 'score1', 'team2', 'score2'.
    
    Returns:
    df (pandas.DataFrame): DataFrame with the added 'winner' column.
    """
    # Create a copy of the DataFrame to avoid modifying the original
    df = df.copy()
    
    # Define a function to determine the winner
    def determine_winner(row):
        if row['score1'] > row['score2']:
            return row['team1']
        elif row['score1'] < row['score2']:
            return row['team2']
        else:
            # If scores are equal, randomly choose a winner
            return random.choice([row['team1'], row['team2']])
    
    # Apply the function to each row and create a new 'winner' column
    df['winner'] = df.apply(determine_winner, axis=1)
    
    return df