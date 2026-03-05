
import pandas as pd
import random

def task_func(df):
    # Define a function to determine the winner based on scores
    def determine_winner(row):
        if row['score_team1'] > row['score_team2']:
            return row['team1']
        elif row['score_team1'] < row['score_team2']:
            return row['team2']
        else:
            return random.choice([row['team1'], row['team2']])
    
    # Apply the determine_winner function to each row and create a new 'winner' column
    df['winner'] = df.apply(determine_winner, axis=1)
    
    return df