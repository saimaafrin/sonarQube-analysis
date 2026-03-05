import matplotlib.pyplot as plt
import pandas as pd
def task_func(temperatures):
    # Check if the input DataFrame is empty
    if temperatures.empty:
        raise ValueError("Input DataFrame is empty")
    
    # Check if the input DataFrame has the expected columns
    expected_columns = {'Date', 'Temperature'}
    if not expected_columns.issubset(temperatures.columns):
        raise ValueError("Input DataFrame does not have the expected columns")
    
    # Convert the 'Date' column to datetime format
    temperatures['Date'] = pd.to_datetime(temperatures['Date'])
    
    # Set the 'Date' column as the index
    temperatures.set_index('Date', inplace=True)
    
    # Plot the temperature data
    fig, ax = plt.subplots()
    ax.plot(temperatures['Temperature'], label='Daily Temperatures in New York')
    
    # Set the font to Arial
    ax.xaxis.label.set_fontname('Arial')
    ax.yaxis.label.set_fontname('Arial')
    ax.title.set_fontname('Arial')
    
    # Set the labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Daily Temperatures in New York')
    
    # Return the Axes object
    return ax