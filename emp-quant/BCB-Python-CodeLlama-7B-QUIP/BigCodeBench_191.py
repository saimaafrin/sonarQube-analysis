
import random
from scipy import stats

def task_func(animals, mean):
    def poisson_dist(x, mu):
        return stats.poisson.pmf(x, mu)

    def generate_sales(n_customers, animals):
        sales = {animal: 0 for animal in animals}
        for i in range(n_customers):
            animal = random.choice(animals)
            sales[animal] += 1
        return sales

    def poisson_sales(n_customers, animals, mu):
        sales = generate_sales(n_customers, animals)
        for animal in sales:
            sales[animal] = poisson_dist(sales[animal], mu)
        return sales

    return poisson_sales(n_customers, animals, mu)