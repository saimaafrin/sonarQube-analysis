import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
TARGET_VALUES = np.array([1, 3, 4])
def task_func(df):
    """
    Replace all elements in DataFrame columns that do not exist in the TARGET_VALUES array with zeros, then perform a Box-Cox transformation on each column (if data is not constant, add 1 to account for zeros) and display the resulting KDE plots.
    """
    # Replace all elements in DataFrame columns that do not exist in the TARGET_VALUES array with zeros
    for col in df.columns:
        df[col] = df[col].replace(to_replace=np.setdiff1d(df[col].unique(), TARGET_VALUES), value=0)

    # Perform Box-Cox transformation on each column
    for col in df.columns:
        if df[col].nunique() > 1:
            df[col] = np.log(df[col] + 1)

    # Display KDE plots of the transformed columns
    fig, axs = plt.subplots(ncols=len(df.columns), figsize=(10, 10))
    for i, col in enumerate(df.columns):
        sns.kdeplot(df[col], ax=axs[i])
        axs[i].set_title(f"KDE plot of {col}")
    plt.show()

    return df, fig
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [1, 2, 3, 4, 5], "C": [1, 2, 3, 4, 5]})