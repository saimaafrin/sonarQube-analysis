
import random
import matplotlib.pyplot as plt

def task_func(points: int):
    x = list(range(points))
    y = [random.random() for _ in range(points)]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    return y, ax