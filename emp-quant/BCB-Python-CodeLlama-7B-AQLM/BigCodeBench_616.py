from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000
def task_func(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    """
    Generate a Dataframe to show the football match results of teams 'Team' with random goals 'Goals' and
    penalties 'Penalty Cost', and create a bar plot of the results. Penalties are converted into fines according to the
    penalty costs.

    Parameters:
    - goals (int): The maximum number of goals a team can score in a match.
    - penalties (int): The maximum number of penalties a team can receive in a match.
    - teams (list of str, optional): A list of team names. Default is ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'].
    - penalty_cost (int, optional): Cost of a penalty in dollars. Default is 1000.
    - rng_seed (int, optional): Random seed for reproducibility. Default is None.

    Returns:
    - DataFrame: A pandas DataFrame containing columns for teams, their goals, and penalty costs.
    - Axes: A matplotlib Axes object representing the bar plot of the results.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - random

    Example:
    >>> seed(42)  # Setting seed for reproducibility
    >>> df, ax = task_func(5, 3, rng_seed=42)
    >>> isinstance(df, pd.DataFrame) and 'Team' in df.columns and 'Goals' in df.columns and 'Penalty Cost' in df.columns
    True
    >>> all(df['Goals'] <= 5) and all(df['Penalty Cost'] <= 3000)  # Goals and penalties are within expected range
    True
    """
    # Generate random goals and penalties
    if rng_seed is not None:
        seed(rng_seed)
    goals = [randint(0, goals) for _ in range(len(teams))]
    penalties = [randint(0, penalties) for _ in range(len(teams))]

    # Create DataFrame
    df = pd.DataFrame(data={'Team': teams, 'Goals': goals, 'Penalty Cost': penalties})

    # Create bar plot
    ax = df.plot.bar(x='Team', y=['Goals', 'Penalty Cost'], rot=0, figsize=(10, 5))
    ax.set_ylabel('Goals and Penalty Cost')
    ax.set_title('Football Match Results')
    ax.set_xlabel('Teams')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_ylim(0, max(goals) + max(penalties) + 1)
    ax.legend(loc='upper left')

    return df, ax