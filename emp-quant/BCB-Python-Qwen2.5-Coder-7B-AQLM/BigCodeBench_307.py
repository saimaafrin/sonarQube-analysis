
import seaborn as sns
import matplotlib.pyplot as plt
import random

def task_func(list_of_lists, seed=0):
    random.seed(seed)
    for sublist in list_of_lists:
        if not sublist:
            sublist.extend(random.sample(range(0, 101), 5))
    
    combined_data = [item for sublist in list_of_lists for item in sublist]
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(combined_data, bins=20, kde=True)
    plt.title('Histogram of Combined Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    return ax