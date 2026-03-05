
from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd

# Constants (they can be overridden with default parameters)
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    if rng_seed is not None:
        seed(rng_seed)
    
    # Generate random goals and penalties for each team
    team_data = {
        'Team': teams,
        'Goals': [randint(0, goals) for _ in teams],
        'Penalty Cost': [randint(0, penalties) for _ in teams]
    }
    
    # Convert penalties into fines
    team_data['Fine'] = team_data['Penalty Cost'] * penalty_cost
    
    # Create DataFrame
    df = pd.DataFrame(team_data)
    
    # Create bar plot
    fig, ax = plt.subplots()
    ax.bar(df['Team'], df['Goals'], color='blue', label='Goals')
    ax.bar(df['Team'], df['Fine'], bottom=df['Goals'], color='red', label='Fines')
    ax.set_xlabel('Teams')
    ax.set_ylabel('Points')
    ax.set_title('Football Match Results')
    ax.legend()
    
    return df, ax