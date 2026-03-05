
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if the DataFrame has columns
    if not df.columns:
        raise ValueError("DataFrame must have at least one column")
    
    # Get the last column of the DataFrame
    last_column = df.iloc[:, -1]
    
    # Create an imputer that uses the mean value to impute missing values
    imputer = SimpleImputer(strategy='mean')
    
    # Fit the imputer on the last column and transform it
    df.iloc[:, -1] = imputer.fit_transform(df.iloc[:, -1].values.reshape(-1, 1))
    
    # Create a box plot of the last column
    plt.figure()
    boxplot = sns.boxplot(x=df.iloc[:, -1])
    
    # Return the DataFrame with the imputed values and the Axes object with the box plot
    return df, boxplot