from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    """
    Generate a DataFrame to show the football match results of teams 'teams' with random goals 'goals' and penalties 'penalties', and create a bar plot of the results. Penalties are converted into fines according to the penalty costs.

    Parameters
    ----------
    goals : int
        The number of goals scored by each team.
    penalties : int
        The number of penalties taken by each team.
    teams : list of str, optional
        The names of the teams.
    penalty_cost : int, optional
        The cost of a penalty in dollars.
    rng_seed : int, optional
        The seed for the random number generator.

    Returns
    -------
    DataFrame
        A pandas DataFrame containing columns for teams, their goals, and penalty costs.
    Axes
        A matplotlib Axes object representing the bar plot of the results.
    """
    # Set the random number generator seed if provided
    if rng_seed is not None:
        seed(rng_seed)

    # Generate random goals and penalties for each team
    results = []
    for team in teams:
        goals = randint(0, goals)
        penalties = randint(0, penalties)
        results.append((team, goals, penalties))

    # Convert penalties into fines
    fines = [penalty_cost * penalty for team, goals, penalty in results]

    # Create a DataFrame with the results
    df = pd.DataFrame(results, columns=['Team', 'Goals', 'Penalties'])
    df['Fines'] = fines

    # Create a bar plot of the results
    fig, ax = plt.subplots()
    ax.bar(df['Team'], df['Goals'], label='Goals')
    ax.bar(df['Team'], df['Penalties'], bottom=df['Goals'], label='Penalties')
    ax.bar(df['Team'], df['Fines'], bottom=df['Goals'] + df['Penalties'], label='Fines')
    ax.set_xlabel('Team')
    ax.set_ylabel('Goals/Penalties/Fines')
    ax.legend()

    return df, ax
goals = 10
penalties = 5
teams = ['Team A', 'Team B', 'Team C']
penalty_cost = 100
rng_seed = 42