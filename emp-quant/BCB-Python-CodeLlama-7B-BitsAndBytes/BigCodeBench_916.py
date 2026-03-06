
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

    # Create a tuple containing the two axes objects
    return (ax1, ax2)

# Load the stock data
df = pd.read_csv("stock_data.csv")

# Call the task function and get the tuple of axes objects
axes = task_func(df)

# Show the plot
plt.show()