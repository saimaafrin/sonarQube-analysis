
from random import randint, seed
import pandas as pd

# Method
def task_func(goals, penalties, rng_seed=None):
    # Set the random seed for reproducibility
    if rng_seed is not None:
        seed(rng_seed)

    # Initialize a list to store the results
    results = []

    # Loop through each team and generate a random number of goals and penalties
    for team in goals:
        # Generate a random number of goals
        goals_scored = randint(0, goals[team])

        # Generate a random number of penalties
        penalties_taken = randint(0, penalties[team])

        # Convert penalties into fines
        fines = penalties_taken * 100

        # Add the results to the list
        results.append({'Team': team, 'Match Result': goals_scored + fines})

    # Create a DataFrame from the results
    df = pd.DataFrame(results, columns=['Team', 'Match Result'])

    return df

# Generate the results
df = task_func(goals, penalties, rng_seed=42)

# Print the results
print(df)