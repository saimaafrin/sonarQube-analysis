
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(list_of_pairs):
    # Create a Pandas DataFrame from the list of pairs
    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])

    # Visualize the data with a bar chart
    fig, ax = plt.subplots()
    ax.bar(df['Category'], df['Value'])
    ax.set_title('Category vs Value')
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')
    ax.set_xticklabels(df['Category'])
    ax.set_yticklabels(df['Value'])
    plt.show()

    return df, fig