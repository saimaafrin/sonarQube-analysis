
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(df: pd.DataFrame) -> tuple:
    # Ensure the DataFrame has a column named 'close' for stock closing prices
    if 'close' not in df.columns:
        raise ValueError("DataFrame must contain a column named 'close'")

    # Create a figure with a single subplot
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Box plot of closing prices
    sns.boxplot(x=df['close'], ax=ax[0])
    ax[0].set_title('Box Plot of Closing Prices')

    # Histogram of closing prices
    sns.histplot(df['close'], ax=ax[1], kde=True)
    ax[1].set_title('Histogram of Closing Prices')

    # Return the axes objects
    return ax[0], ax[1]