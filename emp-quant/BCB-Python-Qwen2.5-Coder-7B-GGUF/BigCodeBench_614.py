
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(goals, penalties):
    # Create a DataFrame from the input data
    data = {'Team': range(1, len(goals) + 1), 'Goals': goals, 'Penalties': penalties}
    df = pd.DataFrame(data)
    
    # Create a pairplot visualization using seaborn
    pairplot = sns.pairplot(df, vars=['Goals', 'Penalties'], kind='reg')
    
    # Display the plot
    plt.show()
    
    # Return the DataFrame and the Axes object
    return df, pairplot.axes