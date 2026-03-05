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
        The number of goals scored by each team in the match.
    penalties : int
        The number of penalties taken by each team in the match.
    teams : list of str, optional
        The names of the teams participating in the match.
    penalty_cost : int, optional
        The cost of each penalty in dollars.
    rng_seed : int, optional
        The seed for the random number generator.

    Returns
    -------
    DataFrame : pandas.DataFrame
        A pandas DataFrame containing columns for teams, their goals, and penalty costs.
    Axes : matplotlib.axes.Axes
        A matplotlib Axes object representing the bar plot of the results.
    """
    # Set the random number generator seed
    if rng_seed is not None:
        seed(rng_seed)

    # Generate the random goals and penalties
    goals_list = [randint(0, goals) for _ in range(len(teams))]
    penalties_list = [randint(0, penalties) for _ in range(len(teams))]

    # Convert penalties into fines
    fines_list = [penalty_cost * penalty for penalty in penalties_list]

    # Create the DataFrame
    df = pd.DataFrame({'Team': teams, 'Goals': goals_list, 'Penalties': penalties_list, 'Fines': fines_list})

    # Create the bar plot
    fig, ax = plt.subplots()
    ax.bar(df['Team'], df['Goals'], label='Goals')
    ax.bar(df['Team'], df['Penalties'], bottom=df['Goals'], label='Penalties')
    ax.bar(df['Team'], df['Fines'], bottom=df['Goals'] + df['Penalties'], label='Fines')
    ax.set_xlabel('Team')
    ax.set_ylabel('Goals/Penalties/Fines')
    ax.legend()

    return df, ax
goals = 5
penalties = 2
teams = ['Team A', 'Team B', 'Team C']
penalty_cost = 1000
rng_seed = 42