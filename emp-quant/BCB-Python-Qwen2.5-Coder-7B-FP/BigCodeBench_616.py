from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    """
    Generates a DataFrame with football match results and creates a bar plot of the results.
    
    Parameters:
    - goals: A list of integers representing the goals scored by each team.
    - penalties: A list of integers representing the penalties scored by each team.
    - teams: A list of strings representing the team names.
    - penalty_cost: An integer representing the cost of each penalty in dollars.
    - rng_seed: An integer representing the seed for the random number generator.
    
    Returns:
    - A pandas DataFrame containing columns for teams, their goals, and penalty costs.
    - A matplotlib Axes object representing the bar plot of the results.
    """
    if rng_seed is not None:
        seed(rng_seed)
    
    # Create a DataFrame with team names, goals, and penalty costs
    data = {
        'Team': teams,
        'Goals': goals,
        'Penalty Cost': [penalty * penalty_cost for penalty in penalties]
    }
    df = pd.DataFrame(data)
    
    # Create a bar plot of the results
    fig, ax = plt.subplots()
    ax.bar(df['Team'], df['Goals'], label='Goals')
    ax.bar(df['Team'], df['Penalty Cost'], bottom=df['Goals'], label='Penalty Cost')
    ax.set_xlabel('Teams')
    ax.set_ylabel('Points')
    ax.set_title('Football Match Results')
    ax.legend()
    
    return df, ax