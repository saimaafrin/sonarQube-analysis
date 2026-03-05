from datetime import datetime
import random
import matplotlib.pyplot as plt
def task_func(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    num_ints = date.day
    ints = [random.randint(1, 100) for _ in range(num_ints)]
    fig, ax = plt.subplots()
    ax.plot(ints)
    return ax
date_str = '2023-02-28'