
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Constants
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]

def task_func(date_str, booking_data):
    """
    Generates a status report of room bookings for a specified date and displays a bar plot.

    Parameters:
    - date_str (str): The date string in "yyyy-mm-dd" format.
    - booking_data (dict): A dictionary where keys are room names and values are lists of tuples (booking_start_date, booking_end_date).

    Returns:
    - DataFrame: A pandas DataFrame containing booking status for each room.
    - matplotlib.pyplot.Axes: A matplotlib Axes object for the bar plot of booking statuses.
    """
    # Validate date format and check if it's a past date
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if date_obj < datetime.now():
            raise ValueError("Date must be in the future.")
    except ValueError as e:
        raise ValueError(f"Invalid date format. Please use 'yyyy-mm-dd'.") from e
    
    # Initialize a dictionary to store booking status for each room
    room_status = {room: 0 for room in ROOMS}
    
    # Check each booking for the given date
    for room, bookings in booking_data.items():
        for start_date, end_date in bookings:
            if start_date <= date_obj <= end_date:
                room_status[room] += 1
    
    # Create a DataFrame from the room status dictionary
    df = pd.DataFrame(list(room_status.items()), columns=["Room", "Bookings"])
    
    # Plotting the bar chart
    fig, ax = plt.subplots()
    ax.bar(df["Room"], df["Bookings"], color='blue')
    ax.set_xlabel('Rooms')
    ax.set_ylabel('Number of Bookings')
    ax.set_title('Room Booking Status on {}'.format(date_str))
    
    return df, ax