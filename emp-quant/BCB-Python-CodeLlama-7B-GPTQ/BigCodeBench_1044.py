import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]
def task_func(date_str, booking_data):
    """
    Generates a status report of room bookings for a specified date and displays a bar plot representing the booking statuses of various rooms.
    """
    # Validate the date
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please provide a date in the format 'yyyy-mm-dd'.")
    if date < datetime.now().date():
        raise ValueError("The date provided is in the past. Please provide a future date.")

    # Compile a booking status report
    booking_status = {}
    for room in ROOMS:
        booking_status[room] = booking_data.get(room, {}).get(date_str, "Unbooked")

    # Visualize the data in a bar plot
    fig, ax = plt.subplots()
    ax.bar(ROOMS, booking_status.values())
    ax.set_xlabel("Rooms")
    ax.set_ylabel("Booking Status")
    ax.set_title("Booking Status Report for {}".format(date_str))
    plt.show()

    # Return the DataFrame and matplotlib.pyplot.Axes
    return pd.DataFrame(booking_status, index=ROOMS), ax