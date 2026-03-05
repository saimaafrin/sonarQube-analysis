
import collections
import random
from queue import PriorityQueue

def task_func(number_teams=5):
    # Create a dictionary to store team names and their points
    teams = {f"Team {i}": random.randint(1, 100) for i in range(1, number_teams + 1)}
    
    # Use PriorityQueue to sort teams by points in descending order
    pq = PriorityQueue()
    for team, points in teams.items():
        pq.put((-points, team))  # Negative points for max-heap behavior
    
    # Create an OrderedDict to store the sorted teams
    sorted_teams = collections.OrderedDict()
    while not pq.empty():
        _, team = pq.get()
        sorted_teams[team] = teams[team]
    
    return sorted_teams