import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df):
    """
    Impute missing values in the last column of the dataframe using mean imputation,
    then create a box plot to visualize the distribution of data in the last column.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame with at least one column.
    
    Returns:
    pd.DataFrame: DataFrame with the imputed last column.
    Axes: Matplotlib Axes object with the boxplot of the last column.
    
    Raises:
    ValueError: If the input is not a DataFrame or has no columns.
    """
    # Check if the input is a DataFrame and has at least one column
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    # Get the last column of the DataFrame
    last_column = df.iloc[:, -1]
    
    # Check if the last column has missing values
    if last_column.isnull().any():
        # Create an imputer object for mean imputation
        imputer = SimpleImputer(strategy='mean')
        
        # Reshape the last column to fit the imputer
        last_column_reshaped = last_column.values.reshape(-1, 1)
        
        # Perform mean imputation
        imputed_last_column = imputer.fit_transform(last_column_reshaped)
        
        # Replace the original last column with the imputed values
        df.iloc[:, -1] = imputed_last_column.flatten()
    
    # Create a box plot of the last column
    boxplot = sns.boxplot(x=df.iloc[:, -1])
    
    # Return the DataFrame with the imputed last column and the box plot
    return df, boxplot