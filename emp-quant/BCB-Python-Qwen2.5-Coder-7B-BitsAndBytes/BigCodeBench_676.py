
import pandas as pd
import random

def task_func(df):
    # Ensure the DataFrame has the required columns
    if not {'team1', 'score1', 'team2', 'score2'}.issubset(df.columns):
        raise ValueError("DataFrame must contain columns: 'team1', 'score1', 'team2', 'score2'")
    
    # Create a new column 'winner'
    def determine_winner(row):
        if row['score1'] > row['score2']:
            return row['team1']
        elif row['score1'] < row['score2']:
            return row['team2']
        else:
            return random.choice([row['team1'], row['team2']])
    
    df['winner'] = df.apply(determine_winner, axis=1)
    
    return df