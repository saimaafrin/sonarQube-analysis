
import random
import string
import matplotlib.pyplot as plt

def task_func(elements, seed=100):
    random.seed(seed)
    formatted_elements = []
    for element in elements:
        formatted_elements.append(f"{random.choice(string.ascii_letters + string.digits)}")
    plt.hist(formatted_elements, bins=26)
    plt.xlabel("Characters")
    plt.ylabel("Count")
    plt.show()
    return formatted_elements