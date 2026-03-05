
import seaborn as sns
import matplotlib.pyplot as plt
import random

def task_func(list_of_lists, seed=0):
    random.seed(seed)
    combined_data = []
    
    for sublist in list_of_lists:
        if not sublist:
            combined_data.extend([random.randint(0, 100) for _ in range(5)])
        else:
            combined_data.extend(sublist)
    
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(combined_data, bins=20, kde=True)
    plt.title('Histogram of Combined Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
    return ax