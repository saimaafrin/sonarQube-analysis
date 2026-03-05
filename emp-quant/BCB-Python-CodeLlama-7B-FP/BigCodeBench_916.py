import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(df: pd.DataFrame) -> tuple:
    """
    Visualize the distribution of stock closing prices using both a box plot and a histogram within a single figure.
    This function is designed to help understand the spread, central tendency, and the distribution shape of stock closing prices.
    """
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Create a box plot of closing prices
    sns.boxplot(x="Close", data=df, ax=ax1)
    ax1.set_title("Box Plot of Closing Prices")

    # Create a histogram of closing prices
    sns.histplot(x="Close", data=df, ax=ax2)
    ax2.set_title("Histogram of Closing Prices")

    # Return the two subplots
    return (ax1, ax2)
df = pd.read_csv("stock_prices.csv")