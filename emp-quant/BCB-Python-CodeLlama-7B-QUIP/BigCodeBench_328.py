
import collections
import random
from queue import PriorityQueue

def task_func(number_teams=5):
    teams = ["Team " + str(i) for i in range(1, number_teams + 1)]
    points = [random.randint(100, 1000) for i in range(number_teams)]
    ranking = collections.OrderedDict(zip(teams, points))
    ranking = PriorityQueue(ranking, key=lambda x: x[1])
    return ranking