
import pandas as pd
import random

def task_func(df):
    # Add a new column to the DataFrame for the winner
    df['winner'] = None

    # Iterate over each row in the DataFrame
    for i in range(len(df)):
        # Get the scores for the two teams in the current match
        team1_score = df.iloc[i]['team1_score']
        team2_score = df.iloc[i]['team2_score']

        # If the scores are equal, randomly decide the winner
        if team1_score == team2_score:
            df.iloc[i]['winner'] = random.choice([df.iloc[i]['team1'], df.iloc[i]['team2']])
        # Otherwise, set the winner to the team with the higher score
        else:
            df.iloc[i]['winner'] = df.iloc[i]['team1_score'] > df.iloc[i]['team2_score']

    return df

# Call the function and print the resulting DataFrame
print(task_func(df))