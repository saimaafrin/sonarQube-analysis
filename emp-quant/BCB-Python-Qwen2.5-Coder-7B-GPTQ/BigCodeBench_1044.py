import pandas as pd
from datetime import datetime
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]
def task_func(date_str, booking_data):
    # Validate the date format and check if it's a past date
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if date_obj < datetime.now():
            raise ValueError("Date must be in the future.")
    except ValueError as e:
        raise ValueError("Invalid date format or past date.") from e

    # Compile booking status report
    status_report = {room: "Available" for room in ROOMS}
    for booking in booking_data:
        if booking['date'] == date_str:
            status_report[booking['room']] = booking['status']

    # Create DataFrame
    df = pd.DataFrame(list(status_report.items()), columns=['Room', 'Status'])

    # Create bar plot
    import matplotlib.pyplot as plt
    ax = df.plot(kind='bar', x='Room', y='Status', legend=False)
    ax.set_title(f"Room Booking Status on {date_str}")
    ax.set_xlabel("Room")
    ax.set_ylabel("Status")

    return df, ax