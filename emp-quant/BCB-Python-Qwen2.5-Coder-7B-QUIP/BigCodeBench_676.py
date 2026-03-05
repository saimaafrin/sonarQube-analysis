
import pandas as pd
import random

def task_func(df):
    # Define a function to determine the winner based on scores
    def determine_winner(score1, score2):
        if score1 > score2:
            return team1
        elif score2 > score1:
            return team2
        else:
            return random.choice([team1, team2])

    # Apply the function to each row of the DataFrame
    df['winner'] = df.apply(lambda row: determine_winner(row['score1'], row['score2']), axis=1)

    return df