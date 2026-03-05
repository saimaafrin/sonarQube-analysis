
import random
from datetime import datetime
import matplotlib.pyplot as plt

def task_func(epoch_milliseconds, seed=None):
    if epoch_milliseconds < 0 or epoch_milliseconds > datetime.utcnow().timestamp():
        raise ValueError("Start time must be positive and before the current time")

    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    sales_data = {}
    for category in categories:
        sales_data[category] = []

    start_date = datetime.fromtimestamp(epoch_milliseconds)
    current_date = datetime.utcnow()
    days_since = (current_date - start_date).days

    for i in range(days_since):
        for category in categories:
            sales_data[category].append(random.randint(10, 50))

    fig, ax = plt.subplots()
    ax.plot(sales_data[category])
    ax.set_xlabel("Days since " + start_date.strftime("%Y-%m-%d"))
    ax.set_ylabel("Sales units")
    ax.set_title("Sales trend for different categories")
    ax.set_xlim(0, days_since)
    ax.set_ylim(0, 100)
    ax.legend(categories)
    ax.grid(True)
    return sales_data, ax