
from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression
# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars
def task_func(goals, penalties, rng_seed=None):
    # Set random seed for reproducibility
    if rng_seed:
        seed(rng_seed)
    # Initialize data structure
    data = {'Team': [], 'Goals': [], 'Penalty Cost': []}
    # Generate random goals and penalties for each team
    for team in TEAMS:
        goals = randint(0, 10)
        penalties = randint(0, 10)
        data['Team'].append(team)
        data['Goals'].append(goals)
        data['Penalty Cost'].append(penalties * PENALTY_COST)
    # Train linear regression model
    model = LinearRegression().fit(data['Goals'], data['Penalty Cost'])
    # Predict penalty costs for each team
    predictions = model.predict(data['Goals'])
    # Create dataframe with predicted penalty costs
    df = pd.DataFrame(data, columns=['Team', 'Goals', 'Penalty Cost', 'Predicted Penalty Cost'])
    df['Predicted Penalty Cost'] = predictions
    return df