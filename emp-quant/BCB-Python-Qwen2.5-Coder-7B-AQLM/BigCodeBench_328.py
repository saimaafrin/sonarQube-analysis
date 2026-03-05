
import collections
import random
from queue import PriorityQueue

def task_func(number_teams=5):
    # Create a dictionary to store team names and their points
    teams = {}
    for i in range(1, number_teams + 1):
        teams[f"Team {i}"] = random.randint(1, 100)  # Assign random points between 1 and 100

    # Sort the dictionary by points in descending order
    sorted_teams = collections.OrderedDict(sorted(teams.items(), key=lambda item: item[1], reverse=True))

    return sorted_teams