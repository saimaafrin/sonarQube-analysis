
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.impute import SimpleImputer

def task_func(df):
    # Replace NaN values with the mean of the column
    imputer = SimpleImputer(strategy='mean')
    df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    
    # Calculate the statistics for the DataFrame
    stats = df.describe()
    
    # Create distribution plots for each numeric column
    fig, axes = plt.subplots(nrows=1, ncols=len(df.columns), figsize=(20, 5))
    
    for i, column in enumerate(df.columns):
        sns.kdeplot(df[column], ax=axes[i], kde=True, cut=0)
        axes[i].set_title(f'Distribution of {column}')
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Density')
    
    return df, axes