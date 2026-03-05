
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(df: pd.DataFrame) -> tuple:
    # Create a box plot of the closing prices
    ax1 = sns.boxplot(x="Close", data=df, orient="v", color="lightblue")
    ax1.set_title("Box Plot of Closing Prices")

    # Create a histogram of the closing prices
    ax2 = sns.histplot(x="Close", data=df, color="lightblue")
    ax2.set_title("Histogram of Closing Prices")

    # Create a figure with both the box plot and histogram
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle("Distribution of Stock Closing Prices", fontsize=16)
    ax1.set_ylabel("Close Price")
    ax2.set_ylabel("Frequency")
    ax1.set_xlabel("")
    ax2.set_xlabel("")

    return (ax1, ax2)