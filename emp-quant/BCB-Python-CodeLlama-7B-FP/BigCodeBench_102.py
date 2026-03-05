import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_diabetes
def task_func():
    # Load the diabetes dataset
    diabetes_df = pd.DataFrame(load_diabetes().data, columns=load_diabetes().feature_names)

    # Set the font to Arial
    plt.rcParams['font.family'] = 'Arial'

    # Create a pairplot using seaborn
    sns.pairplot(diabetes_df, hue='Outcome')

    # Return the matplotlib figure and the DataFrame
    return plt.gcf(), diabetes_df