
import matplotlib.pyplot as plt
import pandas as pd

def task_func(temperatures):
    # Check if the input DataFrame is empty
    if temperatures.empty:
        raise ValueError("The input DataFrame is empty.")
    
    # Check if the input DataFrame has the expected columns
    expected_columns = ['Date', 'Temperature']
    if not all(column in temperatures.columns for column in expected_columns):
        raise ValueError("The input DataFrame does not have the expected columns.")
    
    # Convert the 'Date' column to datetime
    temperatures['Date'] = pd.to_datetime(temperatures['Date'])
    
    # Set the 'Date' column as the index
    temperatures.set_index('Date', inplace=True)
    
    # Plot the temperature data
    fig, ax = plt.subplots()
    ax.plot(temperatures.index, temperatures['Temperature'], label='Daily Temperatures')
    
    # Set the font to Arial
    plt.rcParams['font.family'] = 'Arial'
    
    # Set the labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Daily Temperatures in New York')
    
    # Show the legend
    ax.legend()
    
    # Return the Axes object
    return ax