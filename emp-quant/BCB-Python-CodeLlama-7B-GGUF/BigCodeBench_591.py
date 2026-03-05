
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pandas as pd

TEMP_CATEGORIES = ['Cold', 'Normal', 'Hot']
FILE_PATH = 'custom_data.csv'

def task_func(hours, file_path=FILE_PATH):
    # Generate temperature data
    data = {}
    for i in range(hours):
        time = datetime.now()
        temperature = randint(10, 30)
        category = TEMP_CATEGORIES[randint(0, 2)]
        data[time] = {
            'Time': time,
            'Temperature': temperature,
            'Category': category
        }

    # Save data to CSV file
    df = pd.DataFrame.from_dict(data, orient='index')
    df.to_csv(file_path)

    # Plot data
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Temperature'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature')
    ax.set_title('Temperature Data')
    ax.legend()

    return file_path, ax