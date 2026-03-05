
import random
from scipy import stats

def task_func(animals, mean):
    sales_summary = {animal: 0 for animal in animals}
    num_customers = stats.poisson.rvs(mu=mean)
    
    for _ in range(num_customers):
        animal = random.choice(animals)
        sales_summary[animal] += 1
    
    print(sales_summary)
    return sales_summary