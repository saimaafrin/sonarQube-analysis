
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]

def task_func(date_str, booking_data):
    # Validate date format and raise exception if invalid
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Expected format: yyyy-mm-dd")

    # Check if date is in the past
    if date < datetime.now().date():
        raise ValueError("Date is in the past")

    # Compile booking status report
    booking_status = {}
    for room in ROOMS:
        booking_status[room] = booking_data[room][date_str]

    # Create DataFrame
    df = pd.DataFrame(booking_status, index=ROOMS)

    # Create bar plot
    fig, ax = plt.subplots()
    ax.bar(df.index, df.values)
    ax.set_title("Booking Status Report")
    ax.set_xlabel("Room")
    ax.set_ylabel("Booking Status")
    plt.show()

    return df, ax