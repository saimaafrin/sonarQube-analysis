
import pandas as pd
import random

def task_func(df):
    # Create a new column in the DataFrame to store the winner
    df['winner'] = None

    # Iterate over each row in the DataFrame
    for i in range(len(df)):
        # Get the scores for the two teams in the current match
        team1_score = df.iloc[i, 0]
        team2_score = df.iloc[i, 1]

        # Check if the scores are equal
        if team1_score == team2_score:
            # If the scores are equal, randomly decide the winner
            winner = random.choice([0, 1])
        else:
            # If the scores are not equal, the winner is the team with the higher score
            winner = 1 if team1_score > team2_score else 0

        # Set the winner for the current match
        df.iloc[i, 2] = winner

    return df