import csv
import random
DATA = ['Temperature', 'Humidity', 'Pressure']
RANGE = {
    'Temperature': (-50, 50),
    'Humidity': (0, 100),
    'Pressure': (980, 1040)
}
def task_func(file_name="data.csv"):
    """
    Generate a CSV file with weather data for each hour of the current day.

    Parameters:
    file_name (str): The path to the CSV file to be created.
    
    Returns:
    str: The path to the created file.

    Note:
    - The row names for the csv are 'Temperature', 'Humidity', and 'Pressure' 
    - Temperature ranged rom -50 to 50
    - Humidity ranged rom 0 to 100
    - Pressure ranged rom 980 to 1040

    Requirements:
    - os
    - datetime
    - csv
    - random

    Example:
    >>> task_func("data.csv")
    'path/to/data.csv'
    """
    # Get the current date
    today = datetime.date.today()

    # Create the file
    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(DATA)

        # Write the data for each hour of the day
        for hour in range(24):
            # Get the current hour
            hour = datetime.time(hour, 0, 0)

            # Get the current date and time
            date_time = datetime.datetime.combine(today, hour)

            # Write the data for the current hour
            writer.writerow([random.randint(RANGE['Temperature'][0], RANGE['Temperature'][1]),
                             random.randint(RANGE['Humidity'][0], RANGE['Humidity'][1]),
                             random.randint(RANGE['Pressure'][0], RANGE['Pressure'][1])])

    # Return the path to the created file
    return os.path.abspath(file_name)