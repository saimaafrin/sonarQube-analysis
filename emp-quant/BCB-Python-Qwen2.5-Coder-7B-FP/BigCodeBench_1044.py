import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]
def task_func(date_str, booking_data):
    """
    Generates a status report of room bookings for a specified date and displays a bar plot representing the booking statuses of various rooms.
    
    Parameters:
    - date_str (str): The date for which to generate the booking report in "yyyy-mm-dd" format.
    - booking_data (dict): A dictionary where keys are room names and values are lists of booking statuses for each day.
    
    Returns:
    - DataFrame: A pandas DataFrame containing booking status for each room.
    - matplotlib.pyplot.Axes: A matplotlib Axes object for the bar plot of booking statuses.
    
    Raises:
    - ValueError: If `date_str` does not follow the "yyyy-mm-dd" format or is not a valid date.
    - ValueError: If `date_str` refers to a past date.
    """
    # Validate date format and check if it's a past date
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if date_obj < datetime.now():
            raise ValueError("The provided date is in the past.")
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'yyyy-mm-dd' format.") from e
    
    # Prepare data for the DataFrame
    data = {room: booking_data.get(room, [None])[0] for room in ROOMS}
    df = pd.DataFrame([data], index=[date_str])
    
    # Create a bar plot
    ax = df.plot(kind='bar', legend=False)
    ax.set_xlabel('Rooms')
    ax.set_ylabel('Booking Status')
    ax.set_title(f'Room Booking Status on {date_str}')
    
    return df, ax