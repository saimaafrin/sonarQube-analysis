
from datetime import datetime, timedelta
from random import randint
import matplotlib.pyplot as plt
import pandas as pd

TEMP_CATEGORIES = ['Cold', 'Normal', 'Hot']
FILE_PATH = 'custom_data.csv'

def task_func(hours, file_path=FILE_PATH):
    data = {
        'Time': [],
        'Temperature': [],
        'Category': []
    }
    
    for i in range(hours):
        current_time = datetime.now() + timedelta(hours=i)
        temp = randint(10, 40)  # Simulating temperature between 10°C and 40°C
        category = 'Cold' if temp < 20 else 'Normal' if temp < 30 else 'Hot'
        data['Time'].append(current_time)
        data['Temperature'].append(temp)
        data['Category'].append(category)
    
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Temperature'], marker='o')
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Data Over Time')
    ax.grid(True)
    
    return file_path, ax