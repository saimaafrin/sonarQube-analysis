
import pandas as pd
from datetime import datetime

# Constants
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
    """
    # Validate the date format
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("The date_str must be in 'yyyy-mm-dd' format.")
    
    # Check if the date is in the past
    if date_obj < datetime.now():
        raise ValueError("The date_str cannot refer to a past date.")
    
    # Create a DataFrame to store the booking statuses
    booking_df = pd.DataFrame(index=ROOMS)
    
    # Populate the DataFrame with booking statuses
    for room, statuses in booking_data.items():
        if room in ROOMS:
            booking_df.loc[room] = statuses
    
    # Filter the DataFrame for the specified date
    booking_df = booking_df.loc[:, date_obj]
    
    # Create a bar plot of the booking statuses
    import matplotlib.pyplot as plt
    ax = booking_df.plot(kind='bar', figsize=(10, 6))
    ax.set_title(f'Room Booking Status on {date_str}')
    ax.set_xlabel('Room')
    ax.set_ylabel('Booking Status')
    
    return booking_df, ax