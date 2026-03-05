
import random
from datetime import datetime
import matplotlib.pyplot as plt

def task_func(epoch_milliseconds, seed=None):
    if epoch_milliseconds < 0 or epoch_milliseconds > datetime.utcnow().timestamp() * 1000:
        raise ValueError("Start time must be between 0 and current time")

    sales_data = {}
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    for category in categories:
        sales_data[category] = []

    start_date = datetime.fromtimestamp(epoch_milliseconds / 1000)
    current_date = datetime.utcnow()
    days = (current_date - start_date).days

    for day in range(days):
        for category in categories:
            sales = random.randint(10, 50)
            sales_data[category].append(sales)

    fig, ax = plt.subplots()
    ax.set_xlabel('Days since start date')
    ax.set_ylabel('Sales units')
    ax.set_title('Sales Trend')

    for category, sales in sales_data.items():
        ax.plot(sales, label=category)

    ax.legend()

    return sales_data, ax