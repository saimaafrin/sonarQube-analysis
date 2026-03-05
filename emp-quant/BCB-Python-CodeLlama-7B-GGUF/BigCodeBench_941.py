
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_date: str, periods: int, freq: str, random_seed: int = 0) -> (pd.DataFrame, plt.Axes):
    # Generate random sales data
    np.random.seed(random_seed)
    sales_data = np.random.normal(100, 20, size=(periods,))

    # Create a DataFrame with the sales data
    sales_df = pd.DataFrame({'Date': pd.date_range(start_date, periods=periods, freq=freq),
                              'Sales': sales_data})

    # Plot the sales forecast
    fig, ax = plt.subplots()
    ax.plot(sales_df['Date'], sales_df['Sales'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Forecast')

    return (sales_df, ax)