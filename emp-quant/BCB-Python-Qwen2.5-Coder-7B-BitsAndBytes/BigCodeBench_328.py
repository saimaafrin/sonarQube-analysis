
import collections
import random
from queue import PriorityQueue

def task_func(number_teams=5):
    # Create a dictionary to store team names and their points
    teams = {f"Team {i}": random.randint(0, 100) for i in range(1, number_teams + 1)}
    
    # Sort the dictionary by points in descending order using OrderedDict
    sorted_teams = collections.OrderedDict(sorted(teams.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_teams