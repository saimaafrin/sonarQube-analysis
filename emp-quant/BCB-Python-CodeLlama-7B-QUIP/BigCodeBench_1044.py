
import pandas as pd
from datetime import datetime
# Constants
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]
def task_func(date_str, booking_data):
    # Validate the date
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Expected format: yyyy-mm-dd")
    if date < datetime.today():
        raise ValueError("Date must be a future date")
    # Compile the booking status report
    booking_status = {}
    for room in ROOMS:
        booking_status[room] = 0
    for booking in booking_data:
        if booking["date"] == date:
            booking_status[booking["room"]] += 1
    # Visualize the data
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.bar(ROOMS, booking_status.values())
    ax.set_ylabel("Number of bookings")
    ax.set_xlabel("Room")
    ax.set_title("Booking status for {}".format(date))
    plt.show()
    return pd.DataFrame(booking_status)