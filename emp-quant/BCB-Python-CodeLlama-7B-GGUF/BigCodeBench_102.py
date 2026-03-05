
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_diabetes

def task_func():
    # Load the diabetes dataset
    diabetes_data = load_diabetes()
    diabetes_df = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)

    # Set the font to Arial
    plt.rcParams['font.family'] = 'Arial'

    # Create a pairplot using seaborn
    sns.pairplot(diabetes_df, kind='scatter')

    # Return the matplotlib figure and DataFrame
    return plt.gcf(), diabetes_df

# Call the function
fig, df = task_func()

# Show the plot
plt.show()