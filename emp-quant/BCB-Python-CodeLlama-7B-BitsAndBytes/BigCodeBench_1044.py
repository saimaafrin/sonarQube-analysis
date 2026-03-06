
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]

def task_func(date_str, booking_data):
    # Validate the date
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format or past date")

    # Compile the booking status report
    booking_status = {}
    for room in ROOMS:
        booking_status[room] = booking_data[room][date_str]

    # Create the bar plot
    fig, ax = plt.subplots()
    ax.bar(ROOMS, booking_status.values())
    ax.set_title("Booking Status Report")
    ax.set_xlabel("Room")
    ax.set_ylabel("Booking Status")
    ax.set_xticks(ROOMS)
    ax.set_xticklabels(ROOMS)
    ax.set_ylim([0, 1])
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["Available", "Booked"])

    return pd.DataFrame(booking_status), ax

df, ax = task_func(date_str, booking_data)
print(df)
ax.show()