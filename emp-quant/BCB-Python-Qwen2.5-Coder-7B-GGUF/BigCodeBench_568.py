
import inspect
import matplotlib.pyplot as plt
import pandas as pd

def task_func(f_list):
    if any(inspect.islambda(f) for f in f_list):
        raise ValueError("Input contains lambda function")
    
    data = []
    for f in f_list:
        num_args = len(inspect.signature(f).parameters)
        data.append({'Function': f.__name__, 'Number of Arguments': num_args})
    
    df = pd.DataFrame(data)
    
    # Plotting the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df['Function'], df['Number of Arguments'], color='blue')
    plt.xlabel('Function Name')
    plt.ylabel('Number of Arguments')
    plt.title('Number of Arguments per Function')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return df