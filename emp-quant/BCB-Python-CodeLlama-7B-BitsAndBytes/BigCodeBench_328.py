
import collections
import random
from queue import PriorityQueue

def task_func(number_teams=5):
    # Create a dictionary with team names and random points
    teams = {f"Team {i}": random.randint(1, 100) for i in range(1, number_teams + 1)}

    # Create a priority queue with the teams and their points
    pq = PriorityQueue()
    for team, points in teams.items():
        pq.put((points, team))

    # Sort the priority queue in descending order of points
    sorted_teams = collections.OrderedDict()
    while not pq.empty():
        points, team = pq.get()
        sorted_teams[team] = points

    return sorted_teams