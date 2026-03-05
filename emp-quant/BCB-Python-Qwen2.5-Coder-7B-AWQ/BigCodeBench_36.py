import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
TARGET_VALUES = np.array([1, 3, 4])
def task_func(df):
    # Replace values not in TARGET_VALUES with 0
    df = df.apply(lambda x: x.where(x.isin(TARGET_VALUES), 0))
    
    # Perform Box-Cox transformation
    transformed_df = pd.DataFrame()
    for col in df.columns:
        if df[col].nunique() > 1:  # Check if column has more than one unique value
            transformed_col = stats.boxcox(df[col] + 1)[0]  # Add 1 to handle zeros
            transformed_df[col] = transformed_col
        else:
            transformed_df[col] = df[col]  # If constant, keep the value
    
    # Plot KDE plots
    fig, axes = plt.subplots(nrows=len(transformed_df.columns), ncols=1, figsize=(8, 6*len(transformed_df.columns)))
    for i, col in enumerate(transformed_df.columns):
        transformed_df[col].plot(kind='kde', ax=axes[i], title=f'KDE Plot of {col}')
    
    return transformed_df, fig