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
    Axes: A matplotlib Axes object with the boxplot of the last column.
    
    Raises:
    ValueError: If the input is not a DataFrame or has no columns.
    """
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    if df.shape[1] == 0:
        raise ValueError("DataFrame must have at least one column.")
    
    # Impute missing values in the last column using mean imputation
    imputer = SimpleImputer(strategy='mean')
    df.iloc[:, -1] = imputer.fit_transform(df.iloc[:, -1].values.reshape(-1, 1))
    
    # Create a box plot to visualize the distribution of data in the last column
    ax = sns.boxplot(x=df.iloc[:, -1])
    
    return df, ax