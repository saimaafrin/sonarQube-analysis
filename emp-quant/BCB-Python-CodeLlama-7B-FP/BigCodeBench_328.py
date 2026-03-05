import collections
import random
from queue import PriorityQueue
def task_func(number_teams=5):
    """
    Create a random sports ranking and sort it by points in descending order.
    """
    # Create a dictionary to store the team names and points
    teams = {}

    # Generate random team names and points
    for i in range(1, number_teams + 1):
        team_name = f"Team {i}"
        points = random.randint(1, 100)
        teams[team_name] = points

    # Sort the teams by points in descending order
    sorted_teams = sorted(teams.items(), key=lambda x: x[1], reverse=True)

    # Return the sorted teams as an OrderedDict
    return collections.OrderedDict(sorted_teams)