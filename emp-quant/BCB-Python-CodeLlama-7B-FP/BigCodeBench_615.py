from random import randint, seed
import pandas as pd
def task_func(goals, penalties, rng_seed=None):
    # Set random seed
    if rng_seed is not None:
        seed(rng_seed)

    # Initialize DataFrame
    df = pd.DataFrame(columns=['Team', 'Match Result'])

    # Generate random goals and penalties
    for team in goals:
        df = df.append({'Team': team, 'Match Result': randint(0, 10)}, ignore_index=True)
    for team in penalties:
        df = df.append({'Team': team, 'Match Result': randint(0, 10)}, ignore_index=True)

    # Convert penalties to fines
    for index, row in df.iterrows():
        if row['Match Result'] == 10:
            df.loc[index, 'Match Result'] = randint(0, 10)

    return df