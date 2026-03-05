from random import randint, seed
import pandas as pd
def task_func(goals, penalties, rng_seed=None):
    """
    Generate a Pandas DataFrame with columns 'Team' and 'Match Result' of the results of football matches for multiple teams, incorporating random goals and penalties. Penalties are converted into fines using a predefined cost.
    :param goals: A list of integers representing the number of goals scored by each team in a match.
    :param penalties: A list of integers representing the number of penalties taken by each team in a match.
    :param rng_seed: An integer representing the random seed to use for generating random numbers.
    :return: A pandas DataFrame with columns ['Team', 'Match Result'], detailing each team's goals and accumulated fines.
    """
    # Set the random seed if provided
    if rng_seed is not None:
        seed(rng_seed)

    # Initialize the DataFrame
    df = pd.DataFrame(columns=['Team', 'Match Result'])

    # Generate the random goals and penalties
    for i in range(len(goals)):
        df = df.append({'Team': i, 'Match Result': goals[i] + penalties[i] * 10}, ignore_index=True)

    # Return the DataFrame
    return df
goals = [3, 5, 2, 1, 4]
penalties = [2, 3, 1, 2, 1]