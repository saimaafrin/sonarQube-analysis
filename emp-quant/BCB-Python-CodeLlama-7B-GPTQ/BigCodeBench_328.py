import collections
import random
from queue import PriorityQueue
def task_func(number_teams=5):
    """
    Create a random sports ranking and sort it by points in descending order.
    """
    # Create a dictionary to store the team names and points
    teams = {}
    for i in range(1, number_teams + 1):
        team_name = f"Team {i}"
        points = random.randint(1, 100)
        teams[team_name] = points

    # Sort the dictionary by points in descending order
    sorted_teams = collections.OrderedDict(sorted(teams.items(), key=lambda x: x[1], reverse=True))

    # Return the sorted dictionary
    return sorted_teams