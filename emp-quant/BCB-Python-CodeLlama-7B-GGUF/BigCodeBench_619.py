
from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression
# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars
def task_func(goals, penalties, rng_seed=None):
    # Set random seed for reproducibility
    if rng_seed is not None:
        seed(rng_seed)
    # Initialize data frame
    df = pd.DataFrame(columns=['Team', 'Goals', 'Penalty Cost'])
    # Simulate football match results
    for team in TEAMS:
        # Generate random number of goals
        goals = randint(0, 10)
        # Generate random number of penalties
        penalties = randint(0, 3)
        # Calculate penalty cost
        penalty_cost = PENALTY_COST * penalties
        # Add data to data frame
        df = df.append({'Team': team, 'Goals': goals, 'Penalty Cost': penalty_cost}, ignore_index=True)
    # Train linear regression model
    X = df[['Goals']]
    y = df['Penalty Cost']
    model = LinearRegression().fit(X, y)
    return df, model