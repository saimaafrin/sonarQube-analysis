
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=COLUMNS)

    # Group the DataFrame by col1 and col2
    grouped_df = df.groupby(['col1', 'col2'])

    # Create a heatmap of the distribution of values in col3
    sns.heatmap(grouped_df['col3'].value_counts(), annot=True, cmap='Blues')

    # Return the DataFrame and the heatmap
    return df, plt.gca()

df, heatmap = task_func(data)

# Display the heatmap
plt.show()