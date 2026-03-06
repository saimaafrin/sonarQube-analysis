
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    # Check if there are any columns in the DataFrame
    if df.columns.size == 0:
        raise ValueError("DataFrame must contain at least one column.")
    
    # Impute missing values in the last column using mean imputation
    imputer = SimpleImputer(strategy='mean')
    df.iloc[:, -1] = imputer.fit_transform(df.iloc[:, -1].values.reshape(-1, 1))
    
    # Create a box plot to visualize the distribution of data in the last column
    ax = sns.boxplot(x=df.iloc[:, -1])
    plt.show()
    
    return df, ax