import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]
def task_func(date_str, booking_data):
    """
    Generates a status report of room bookings for a specified date and displays a bar plot representing the booking statuses of various rooms.
    Validates the provided date, compiles a booking status report, and visualizes the data in a bar plot.
    Raises ValueError in two scenarios:
        1. If `date_str` does not follow the "yyyy-mm-dd" format or is not a valid date.
        2. If `date_str` refers to a past date.
    Returns:
        DataFrame: A pandas DataFrame containing booking status for each room.
        matplotlib.pyplot.Axes: A matplotlib Axes object for the bar plot of booking statuses.
    """
    # Validate date format
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please provide a date in the format 'yyyy-mm-dd'.")

    # Check if date is in the future
    if date < datetime.now():
        raise ValueError("Date cannot be in the past. Please provide a future date.")

    # Compile booking status report
    booking_status = {}
    for room in ROOMS:
        booking_status[room] = booking_data[room][date_str]

    # Create bar plot
    fig, ax = plt.subplots()
    ax.bar(ROOMS, booking_status.values())
    ax.set_title("Booking Status Report")
    ax.set_xlabel("Room")
    ax.set_ylabel("Booking Status")
    ax.set_xticks(ROOMS)
    ax.set_xticklabels(ROOMS)
    ax.legend()

    return pd.DataFrame(booking_status), ax