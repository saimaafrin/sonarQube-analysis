import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df):
    """
    Impute missing values in the last column of the dataframe using mean imputation,
    then create a box plot to visualize the distribution of data in the last column.
    """
    # Check if input is a DataFrame and has columns
    if not isinstance(df, pd.DataFrame) or df.shape[1] == 0:
        raise ValueError("Input must be a non-empty DataFrame")

    # Impute missing values using mean imputation
    imputer = SimpleImputer(strategy="mean")
    imputed_df = imputer.fit_transform(df)

    # Create box plot of last column
    sns.boxplot(x=imputed_df.iloc[:, -1])
    plt.show()

    # Return imputed DataFrame and box plot Axes
    return imputed_df, plt.gca()