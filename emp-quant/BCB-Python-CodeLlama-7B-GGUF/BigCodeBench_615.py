
from random import randint, seed
import pandas as pd

# Method
def task_func(goals, penalties, rng_seed=None):
    # Set random seed for reproducibility
    if rng_seed is not None:
        seed(rng_seed)

    # Initialize DataFrame with columns for team and match result
    df = pd.DataFrame(columns=['Team', 'Match Result'])

    # Generate random goals and penalties for each team
    for team in goals:
        goals_scored = randint(0, goals[team])
        penalties_taken = randint(0, penalties[team])
        penalties_converted = penalties_taken * 100
        fines_accumulated = penalties_converted * 1000
        match_result = goals_scored - penalties_taken

        # Add row to DataFrame
        df = df.append({'Team': team, 'Match Result': match_result}, ignore_index=True)

    return df

# Generate DataFrame with results
df = task_func(goals, penalties)

# Print DataFrame
print(df)