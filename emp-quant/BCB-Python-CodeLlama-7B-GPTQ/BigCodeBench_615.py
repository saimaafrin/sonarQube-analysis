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
        goals = [randint(0, 5) for _ in range(goals)]
        penalties = [randint(0, 5) for _ in range(penalties)]

        # Convert penalties into fines
        fines = [penalty * 10 for penalty in penalties]

        # Add to DataFrame
        df = df.append({'Team': team, 'Match Result': goals + fines}, ignore_index=True)

    return df