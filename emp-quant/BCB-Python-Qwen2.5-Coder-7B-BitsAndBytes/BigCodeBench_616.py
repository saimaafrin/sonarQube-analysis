
from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd

# Constants (they can be overridden with default parameters)
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    if rng_seed is not None:
        seed(rng_seed)

    # Generate random data for goals and penalties
    team_data = {team: {'Goals': randint(0, goals), 'Penalty Cost': randint(0, penalties)} for team in teams}
    
    # Convert penalty costs to fines
    for team, stats in team_data.items():
        stats['Fine'] = stats['Penalty Cost'] * penalty_cost
    
    # Create a DataFrame from the data
    df = pd.DataFrame(list(team_data.values()), index=list(team_data.keys()))
    
    # Create a bar plot of the results
    fig, ax = plt.subplots()
    bars = ax.bar(df.index, df['Goals'], color='blue')
    ax.set_xlabel('Teams')
    ax.set_ylabel('Goals')
    ax.set_title('Football Match Results')
    
    # Add penalty cost labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{bar.get_height()} ({df.loc[bar.get_x(), "Penalty Cost"]} penalties)', ha='center', va='bottom')
    
    return df, ax