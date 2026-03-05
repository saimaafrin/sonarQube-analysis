
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(df: pd.DataFrame) -> tuple:
    # Set the title for the box plot
    box_plot_title = 'Box Plot of Closing Prices'
    # Set the title for the histogram
    histogram_title = 'Histogram of Closing Prices'

    # Create a new figure with a shared x-axis
    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)

    # Create a box plot for the closing prices
    ax[0].boxplot(df['Close'])
    ax[0].set_title(box_plot_title)

    # Create a histogram for the closing prices
    ax[1].hist(df['Close'])
    ax[1].set_title(histogram_title)

    # Return the tuple of axes
    return (ax[0], ax[1])