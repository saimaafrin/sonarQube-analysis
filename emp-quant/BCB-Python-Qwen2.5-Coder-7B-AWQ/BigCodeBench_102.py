import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_diabetes
def task_func():
    # Load the diabetes dataset
    diabetes_data = load_diabetes()
    
    # Create a DataFrame from the dataset
    df = pd.DataFrame(data=diabetes_data.data, columns=diabetes_data.feature_names)
    df['target'] = diabetes_data.target
    
    # Set the font to Arial
    plt.rcParams['font.family'] = 'Arial'
    
    # Create a pairplot using seaborn
    pairplot_figure = sns.pairplot(df)
    
    # Return the pairplot figure and the DataFrame
    return pairplot_figure, df