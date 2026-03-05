
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
TEMP_CATEGORIES = ['Cold', 'Normal', 'Hot']
FILE_PATH = 'custom_data.csv'
def task_func(hours, file_path=FILE_PATH):
    # Generate temperature data for the specified number of hours
    data = {}
    for i in range(hours):
        data[i] = {
            'Time': datetime.now().strftime("%H:%M:%S"),
            'Temperature': randint(10, 30),
            'Category': TEMP_CATEGORIES[randint(0, 2)]
        }
    # Save the data to a CSV file
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Temperature'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature')
    ax.set_title('Temperature Data')
    ax.legend()
    return file_path, ax