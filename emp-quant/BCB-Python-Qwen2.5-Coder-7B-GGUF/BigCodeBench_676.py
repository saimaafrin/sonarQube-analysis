
import pandas as pd
import random

def task_func(df):
    # Create a new column 'winner' and initialize it with None
    df['winner'] = None
    
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        team1_score = row['team1_score']
        team2_score = row['team2_score']
        
        # Determine the winner based on the scores
        if team1_score > team2_score:
            df.at[index, 'winner'] = row['team1']
        elif team2_score > team1_score:
            df.at[index, 'winner'] = row['team2']
        else:
            # If scores are equal, randomly decide the winner
            if random.choice([True, False]):
                df.at[index, 'winner'] = row['team1']
            else:
                df.at[index, 'winner'] = row['team2']
    
    return df