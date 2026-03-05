import collections
import random
from queue import PriorityQueue
def task_func(number_teams=5):
    """
    Create a random sports ranking and sort it by points in descending order.
    """
    # Create a dictionary of teams and their corresponding points
    teams = {}
    for i in range(1, number_teams + 1):
        teams["Team " + str(i)] = random.randint(1, 100)

    # Create a priority queue to sort the teams by points
    queue = PriorityQueue()
    for team, points in teams.items():
        queue.put((points, team))

    # Sort the teams by points in descending order
    sorted_teams = collections.OrderedDict()
    while not queue.empty():
        points, team = queue.get()
        sorted_teams[team] = points

    return sorted_teams