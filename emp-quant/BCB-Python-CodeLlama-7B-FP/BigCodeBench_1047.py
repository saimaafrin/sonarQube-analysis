from datetime import datetime
import random
import matplotlib.pyplot as plt
def task_func(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    day = date.day
    random_ints = [random.randint(0, 100) for _ in range(day)]
    fig, ax = plt.subplots()
    ax.plot(random_ints)
    return ax