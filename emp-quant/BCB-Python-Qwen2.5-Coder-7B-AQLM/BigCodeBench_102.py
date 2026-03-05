
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_diabetes

def task_func():
    # Set the font to Arial
    plt.rcParams['font.family'] = 'Arial'
    
    # Load the diabetes dataset
    diabetes = load_diabetes()
    
    # Convert the dataset to a DataFrame
    diabetes_df = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
    
    # Create a pairplot using seaborn
    pairplot_figure = sns.pairplot(diabetes_df)
    
    # Return the matplotlib Figure instance and the DataFrame
    return pairplot_figure, diabetes_df