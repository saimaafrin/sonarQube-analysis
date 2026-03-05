import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(list_of_pairs):
    # Create a DataFrame from the list of pairs
    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])
    
    # Create a bar chart using seaborn
    ax = sns.barplot(x='Category', y='Value', data=df)
    
    # Set the title of the bar plot
    ax.set_title('Category vs Value')
    
    # Return the DataFrame and the Axes object
    return df, ax