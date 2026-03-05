import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df):
    # Check if the input is a DataFrame and has at least one column
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    
    # Check if the DataFrame has at least one column
    if df.shape[1] == 0:
        raise ValueError("DataFrame must have at least one column")
    
    # Get the last column of the DataFrame
    last_column = df.iloc[:, -1]
    
    # Check if the last column has any missing values
    if last_column.isnull().any():
        # Create an imputer object for mean imputation
        imputer = SimpleImputer(strategy='mean')
        
        # Fit and transform the last column to impute missing values
        imputed_column = imputer.fit_transform(last_column.values.reshape(-1, 1))
        
        # Replace the original last column with the imputed values
        df.iloc[:, -1] = imputed_column.flatten()
    
    # Create a box plot of the last column
    ax = sns.boxplot(x=df.iloc[:, -1])
    
    # Return the DataFrame with imputed values and the Axes object with the box plot
    return df, ax