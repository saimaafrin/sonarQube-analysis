from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    """
    Generates a DataFrame with football match results and creates a bar plot of the results.
    
    Parameters:
    - goals: A list of integers representing the number of goals scored by each team.
    - penalties: A list of integers representing the number of penalties scored by each team.
    - teams: A list of strings representing the team names.
    - penalty_cost: An integer representing the cost of each penalty in dollars.
    - rng_seed: An integer representing the seed for the random number generator.
    
    Returns:
    - A pandas DataFrame containing columns for teams, their goals, and penalty costs.
    - A matplotlib Axes object representing the bar plot of the results.
    """
    if rng_seed is not None:
        seed(rng_seed)
    
    # Calculate fines for penalties
    fines = [penalty * penalty_cost for penalty in penalties]
    
    # Create DataFrame
    data = {
        'Team': teams,
        'Goals': goals,
        'Penalty Cost': fines
    }
    df = pd.DataFrame(data)
    
    # Create bar plot
    fig, ax = plt.subplots()
    ax.bar(df['Team'], df['Goals'], color='blue', label='Goals')
    ax.bar(df['Team'], df['Penalty Cost'], bottom=df['Goals'], color='red', label='Penalties')
    ax.set_xlabel('Teams')
    ax.set_ylabel('Scores')
    ax.set_title('Football Match Results')
    ax.legend()
    
    return df, ax
goals = [randint(0, 10) for _ in TEAMS]
penalties = [randint(0, 5) for _ in TEAMS]