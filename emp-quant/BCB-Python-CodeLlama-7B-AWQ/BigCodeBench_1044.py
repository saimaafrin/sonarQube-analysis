import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]
def task_func(date_str, booking_data):
    """
    Generates a status report of room bookings for a specified date and displays a bar plot representing the booking statuses of various rooms.
    """
    # Validate date
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please provide a date in the format 'yyyy-mm-dd'.")
    if date < datetime.now().date():
        raise ValueError("Cannot generate report for past dates.")

    # Compile booking status report
    booking_status_report = pd.DataFrame(columns=ROOMS)
    for room in ROOMS:
        booking_status_report[room] = booking_data[room][date_str]

    # Visualize booking statuses
    fig, ax = plt.subplots()
    ax.bar(ROOMS, booking_status_report.values)
    ax.set_title("Booking Statuses for {}".format(date_str))
    ax.set_xlabel("Room")
    ax.set_ylabel("Booking Status")
    ax.set_xticks(range(len(ROOMS)))
    ax.set_xticklabels(ROOMS)
    plt.show()

    return booking_status_report, ax