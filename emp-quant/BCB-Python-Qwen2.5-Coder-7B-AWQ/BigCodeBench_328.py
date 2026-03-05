import collections
import random
from queue import PriorityQueue
def task_func(number_teams=5):
    # Create a dictionary to store team names and their points
    teams = {f"Team {i+1}": random.randint(1, 100) for i in range(number_teams)}
    
    # Sort the dictionary by points in descending order using OrderedDict
    sorted_teams = collections.OrderedDict(sorted(teams.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_teams