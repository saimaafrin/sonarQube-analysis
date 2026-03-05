
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a DataFrame and has columns
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    
    # Get the last column of the DataFrame
    last_column = df.columns[-1]
    
    # Create an imputer object for mean imputation
    imputer = SimpleImputer(strategy='mean')
    
    # Fit and transform the last column
    df[last_column] = imputer.fit_transform(df[[last_column]])
    
    # Create a box plot of the last column
    fig, ax = plt.subplots()
    sns.boxplot(x=df[last_column], ax=ax)
    
    return df, ax