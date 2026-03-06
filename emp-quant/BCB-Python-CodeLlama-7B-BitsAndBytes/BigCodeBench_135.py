
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Check if input is a DataFrame and has columns
    if not isinstance(df, pd.DataFrame) or df.shape[1] == 0:
        raise ValueError("Input must be a DataFrame with columns")

    # Impute missing values in last column using mean imputation
    imputer = SimpleImputer(strategy="mean")
    imputed_df = imputer.fit_transform(df)

    # Create box plot of last column
    sns.boxplot(data=imputed_df, x="last_column")
    plt.show()

    # Return imputed DataFrame and box plot Axes
    return imputed_df, plt.gca()