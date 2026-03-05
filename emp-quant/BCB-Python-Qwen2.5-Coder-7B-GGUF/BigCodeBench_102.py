
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_diabetes

def task_func():
    # Load the diabetes dataset
    diabetes = load_diabetes()
    
    # Convert the dataset to a pandas DataFrame
    df = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
    df['target'] = diabetes.target
    
    # Set the font to Arial
    plt.rcParams['font.family'] = 'Arial'
    
    # Create a pairplot using seaborn
    pairplot = sns.pairplot(df)
    
    # Return the matplotlib Figure instance and the DataFrame
    return pairplot, df