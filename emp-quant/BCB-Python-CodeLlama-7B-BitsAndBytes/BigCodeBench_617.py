
from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
import re

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, rng_seed=None, teams=TEAMS):
    # Generate random match results
    match_results = []
    for team in teams:
        match_results.append({
            'Team': team,
            'Goals': randint(0, 10),
            'Penalty Cost': randint(0, 10) * PENALTY_COST
        })

    # Convert penalties into fines
    for result in match_results:
        if result['Penalty Cost'] > 0:
            result['Fine'] = result['Penalty Cost'] * 0.5

    # Create a DataFrame from the results
    df = pd.DataFrame(match_results)

    # Visualize the data
    plt.figure(figsize=(12, 6))
    plt.bar(df['Team'], df['Goals'])
    plt.xlabel('Team')
    plt.ylabel('Goals')
    plt.title('Match Results')
    plt.show()

    # Analyze the data
    print(df.describe())

# Call the function with some random inputs
task_func(goals=10, penalties=5, rng_seed=42)