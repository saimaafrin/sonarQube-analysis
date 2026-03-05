
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Check if input is a DataFrame and has columns
    if not isinstance(df, pd.DataFrame) or df.shape[1] == 0:
        raise ValueError("Input must be a non-empty DataFrame")

    # Impute missing values in last column using mean imputation
    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    imputed_df = imputer.fit_transform(df)

    # Create box plot of last column
    sns.boxplot(data=imputed_df.iloc[:, -1])
    plt.show()

    # Return imputed DataFrame and box plot Axes
    return imputed_df, plt.gca()