
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    if df.columns.empty:
        raise ValueError("DataFrame must have at least one column.")
    
    # Impute missing values in the last column using mean imputation
    imputer = SimpleImputer(strategy='mean')
    df.iloc[:, -1] = imputer.fit_transform(df.iloc[:, -1].values.reshape(-1, 1))
    
    # Create a box plot to visualize the distribution of data in the last column
    ax = sns.boxplot(x=df.iloc[:, -1])
    plt.title(f'Box Plot of the Imputed Last Column')
    plt.xlabel('Imputed Last Column')
    
    return df, ax