
from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, rng_seed=None):
    # Initialize data frame
    df = pd.DataFrame(columns=['Team', 'Goals', 'Penalty Cost'])

    # Set random seed if provided
    if rng_seed is not None:
        seed(rng_seed)

    # Simulate football match results
    for i in range(goals):
        # Generate random team and goals
        team = TEAMS[randint(0, len(TEAMS) - 1)]
        goals = randint(0, 10)

        # Generate random penalty cost
        penalty_cost = PENALTY_COST * randint(0, 10) / 10

        # Add data to data frame
        df = df.append({'Team': team, 'Goals': goals, 'Penalty Cost': penalty_cost}, ignore_index=True)

    # Train linear regression model
    X = df[['Goals']]
    y = df['Penalty Cost']
    model = LinearRegression().fit(X, y)

    # Return data frame and trained model
    return df, model