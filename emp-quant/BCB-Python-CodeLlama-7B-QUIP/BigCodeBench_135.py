
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    # Check if DataFrame has columns
    if df.shape[1] == 0:
        raise ValueError("DataFrame has no columns")

    # Impute missing values in last column
    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    df_imputed = imputer.fit(df.iloc[:, -1])

    # Create box plot
    fig, ax = plt.subplots()
    sns.boxplot(df_imputed.iloc[:, -1])
    ax.set_xlabel("Value")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of last column")

    return df_imputed, ax