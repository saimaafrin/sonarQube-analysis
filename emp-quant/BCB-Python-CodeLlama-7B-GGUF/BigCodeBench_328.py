
import collections
import random
from queue import PriorityQueue

def task_func(number_teams=5):
    teams = []
    for i in range(1, number_teams+1):
        team_name = f"Team {i}"
        team_points = random.randint(1, 100)
        teams.append((team_name, team_points))

    sorted_teams = sorted(teams, key=lambda x: x[1], reverse=True)

    return collections.OrderedDict(sorted_teams)

print(task_func(5))