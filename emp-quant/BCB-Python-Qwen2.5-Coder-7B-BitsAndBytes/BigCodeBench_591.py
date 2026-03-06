
from datetime import datetime, timedelta
from random import randint
import matplotlib.pyplot as plt
import pandas as pd

TEMP_CATEGORIES = ['Cold', 'Normal', 'Hot']
FILE_PATH = 'custom_data.csv'

def task_func(hours, file_path=FILE_PATH):
    # Initialize the data structure
    data = {'Time': [], 'Temperature': [], 'Category': []}
    
    # Generate data for each hour
    start_time = datetime.now()
    for _ in range(hours):
        current_time = start_time + timedelta(hours=_)
        temp = randint(10, 40)  # Random temperature between 10°C and 40°C
        category = TEMP_CATEGORIES[(temp - 10) // 15]  # Categorize temperature
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
    ax.set_title('Temperature Over Time')
    ax.grid(True)
    
    return file_path, ax