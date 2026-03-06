
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
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        temperature = randint(10, 30)
        category = TEMP_CATEGORIES[temperature // 10]
        data[time] = {'Time': time, 'Temperature': temperature, 'Category': category}

    # Save the data to a CSV file
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Temperature'], label='Temperature')
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature')
    ax.set_title('Temperature Data')
    ax.legend()

    return file_path, ax

# Call the function with the desired number of hours
file_path, ax = task_func(48)

# Print the path of the generated CSV file
print(file_path)

# Show the plot
plt.show()