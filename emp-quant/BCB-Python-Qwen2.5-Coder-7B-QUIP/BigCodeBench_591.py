
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
TEMP_CATEGORIES = ['Cold', 'Normal', 'Hot']
FILE_PATH = 'custom_data.csv'
def task_func(hours, file_path=FILE_PATH):
    # Generate temperature data
    data = {'Time': [], 'Temperature': [], 'Category': []}
    for _ in range(hours):
        time = datetime.now() + pd.Timedelta(seconds=_*60)
        temp = randint(10, 40)  # Random temperature between 10 and 40 degrees
        category = 'Cold' if temp < 20 else 'Normal' if temp < 30 else 'Hot'
        data['Time'].append(time)
        data['Temperature'].append(temp)
        data['Category'].append(category)

    # Save data to CSV
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Temperature'], marker='o')
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature')
    ax.set_title('Temperature Data')
    ax.set_xticklabels(df['Time'], rotation=45, ha='right')

    return file_path, ax