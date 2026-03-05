
import random
from scipy import stats

def task_func(animals, mean):
    sales_summary = {animal: 0 for animal in animals}
    num_customers = stats.poisson.rvs(mu=mean)
    
    for _ in range(num_customers):
        customer_choice = random.choice(animals)
        sales_summary[customer_choice] += 1
    
    print("Sales Summary:")
    for animal, sales in sales_summary.items():
        print(f"{animal}: {sales} sales")
    
    return sales_summary