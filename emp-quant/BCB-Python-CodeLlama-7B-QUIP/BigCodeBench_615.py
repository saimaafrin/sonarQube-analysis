
from random import randint, seed
import pandas as pd

def task_func(goals, penalties, rng_seed=None):
    # Set the random seed for reproducibility
    if rng_seed:
        seed(rng_seed)

    # Create a list of teams
    teams = ['Team 1', 'Team 2', 'Team 3', 'Team 4', 'Team 5']

    # Create a list of matches
    matches = [
        {'Team': teams[i], 'Match Result': randint(0, 100)} for i in range(len(teams))
    ]

    # Convert penalties to fines
    for i in range(len(matches)):
        if matches[i]['Match Result'] == 100:
            matches[i]['Match Result'] = randint(0, 100)

    # Create a DataFrame
    df = pd.DataFrame(matches)

    return df