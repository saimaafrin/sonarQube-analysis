
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Constants
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]

def task_func(date_str, booking_data):
    # Validate the date format and check if it's a past date
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if date_obj < datetime.now():
            raise ValueError("The date provided is a past date.")
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'yyyy-mm-dd' format.") from e
    
    # Compile booking status report
    booking_report = {room: "Available" for room in ROOMS}
    for booking in booking_data:
        if booking['date'] == date_str:
            booking_report[booking['room']] = "Booked"
    
    # Create DataFrame
    df = pd.DataFrame(list(booking_report.items()), columns=['Room', 'Status'])
    
    # Create bar plot
    ax = df.plot(kind='bar', x='Room', y='Status', color=['green' if status == 'Available' else 'red' for status in df['Status']])
    ax.set_title(f'Room Booking Status on {date_str}')
    ax.set_xlabel('Room')
    ax.set_ylabel('Status')
    
    return df, ax