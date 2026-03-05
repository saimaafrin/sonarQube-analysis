
import collections
import random
from queue import PriorityQueue

def task_func(number_teams=5):
    # Generate random points for each team
    teams_points = {f"Team {i}": random.randint(1, 100) for i in range(1, number_teams + 1)}
    
    # Sort the dictionary by points in descending order
    sorted_teams = sorted(teams_points.items(), key=lambda x: x[1], reverse=True)
    
    # Convert the list of tuples back to an OrderedDict
    sorted_dict = collections.OrderedDict(sorted_teams)
    
    return sorted_dict