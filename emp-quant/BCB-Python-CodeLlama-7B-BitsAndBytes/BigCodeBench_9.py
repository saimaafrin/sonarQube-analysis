
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(list_of_pairs):
    # Create a Pandas DataFrame from the list of pairs
    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])

    # Visualize the data using a bar chart
    ax = sns.barplot(x='Category', y='Value', data=df)
    ax.set_title('Category vs Value')

    return df, ax

# Display the bar chart
plt.show()