
from datetime import datetime, timedelta
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
TEMP_CATEGORIES = ['Cold', 'Normal', 'Hot']
FILE_PATH = 'custom_data.csv'

def task_func(hours, file_path=FILE_PATH):
    # Initialize the data dictionary
    data = {'Time': [], 'Temperature': [], 'Category': []}
    
    # Generate data for the specified number of hours
    for i in range(hours):
        current_time = datetime.now() + timedelta(hours=i)
        temp = randint(10, 40)  # Random temperature between 10 and 40 degrees
        category = TEMP_CATEGORIES[(temp - 10) // 10]  # Categorize temperature
        data['Time'].append(current_time)
        data['Temperature'].append(temp)
        data['Category'].append(category)
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    
    # Plot the temperature data
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Temperature'], marker='o')
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Data Over Time')
    
    return file_path, ax