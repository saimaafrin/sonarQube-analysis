import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df):
    """
    Impute missing values in the last column of the dataframe using mean imputation, then create a box plot to visualize the distribution of data in the last column.
    """
    if not isinstance(df, pd.DataFrame) or df.shape[1] == 0:
        raise ValueError("Input must be a non-empty pandas DataFrame")

    # Impute missing values using mean imputation
    imputer = SimpleImputer(strategy="mean")
    imputed_df = imputer.fit_transform(df)

    # Create a box plot of the last column of the dataframe
    sns.boxplot(data=imputed_df.iloc[:, -1])
    plt.show()

    return imputed_df
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})