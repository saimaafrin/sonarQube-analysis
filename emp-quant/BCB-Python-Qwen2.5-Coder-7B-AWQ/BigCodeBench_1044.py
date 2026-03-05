import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]
def task_func(date_str, booking_data):
    """
    Generates a status report of room bookings for a specified date and displays a bar plot representing the booking statuses of various rooms.
    
    Parameters:
    - date_str (str): The date in "yyyy-mm-dd" format for which to generate the booking report.
    - booking_data (dict): A dictionary where keys are room names and values are lists of booking dates.
    
    Returns:
    - DataFrame: A pandas DataFrame containing booking status for each room.
    - matplotlib.pyplot.Axes: A matplotlib Axes object for the bar plot of booking statuses.
    
    Raises:
    - ValueError: If `date_str` does not follow the "yyyy-mm-dd" format or is not a valid date, or if it refers to a past date.
    """
    # Validate the date string
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use 'yyyy-mm-dd'.")
    
    if date < datetime.now():
        raise ValueError("Cannot generate report for a past date.")
    
    # Initialize a dictionary to store booking statuses
    booking_statuses = {room: 0 for room in ROOMS}
    
    # Update booking statuses based on booking data
    for room, dates in booking_data.items():
        if room in ROOMS:
            for booking_date in dates:
                if booking_date == date_str:
                    booking_statuses[room] = 1
    
    # Create a DataFrame from the booking statuses
    df = pd.DataFrame(list(booking_statuses.items()), columns=["Room", "Booked"])
    
    # Create a bar plot
    ax = df.plot(kind='bar', x='Room', y='Booked', legend=False)
    ax.set_title(f'Room Booking Status for {date_str}')
    ax.set_xlabel('Room')
    ax.set_ylabel('Booked')
    
    return df, ax