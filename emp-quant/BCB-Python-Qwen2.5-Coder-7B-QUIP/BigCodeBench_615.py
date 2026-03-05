
from random import randint, seed
import pandas as pd

# Method
def task_func(goals, penalties, rng_seed=None):
    # Set the random seed if provided
    if rng_seed is not None:
        seed(rng_seed)

    # Define the cost of penalties
    penalty_cost = 10  # Example cost for penalties

    # Initialize a list to store the results
    results = []

    # Simulate the matches for multiple teams
    for _ in range(10):  # Simulate 10 matches
        team_name = f"Team {_}"
        goals_scored = randint(0, 10)  # Random number of goals scored
        penalties_received = randint(0, 5)  # Random number of penalties received
        fines = penalties_received * penalty_cost  # Calculate fines for penalties

        # Append the result to the list
        results.append({
            'Team': team_name,
            'Match Result': f"{goals_scored} goals, {penalties_received} penalties, {fines} fines"
        })

    # Convert the list to a pandas DataFrame
    df = pd.DataFrame(results)

    return df