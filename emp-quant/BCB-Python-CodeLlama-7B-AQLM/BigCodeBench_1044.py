import pandas as pd
from datetime import datetime
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]
def task_func(date_str, booking_data):
    """
    This function generates a status report of room bookings for a specified date
    and displays a bar plot representing the booking statuses of various rooms.
    It validates the provided date, compiles a booking status report, and visualizes
    the data in a bar plot.

    Parameters:
    - date_str (str): The date for which the booking status needs to be checked,
                      in "yyyy-mm-dd" format. The function validates this date.
    - booking_data (dict): A dictionary with room names as keys and booking statuses
                           as values. The keys should match the rooms listed in the ROOMS constant.

    Returns:
    - DataFrame: A pandas DataFrame containing booking status for each room.
    - matplotlib.pyplot.Axes: A matplotlib Axes object for the bar plot of booking statuses.

    Raises:
    - ValueError: Raised in two scenarios:
                  1. If `date_str` does not follow the "yyyy-mm-dd" format or is not a valid date.
                  2. If `date_str` refers to a past date.

    Requirements:
    - pandas
    - datetime

    Example:
    >>> future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    >>> booking_info = {"Room1": "Booked", "Room2": "Available"}
    >>> report_df, ax = task_func(future_date, booking_info)
    >>> print(report_df)
        Room Booking Status
    0  Room1         Booked
    1  Room2      Available
    2  Room3     Not Listed
    3  Room4     Not Listed
    4  Room5     Not Listed
    """
    # Validate date
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please provide a date in 'yyyy-mm-dd' format.")
    if date < datetime.now():
        raise ValueError("Cannot check booking status for a past date.")

    # Compile report
    report_df = pd.DataFrame(columns=["Room", "Booking Status"])
    for room in ROOMS:
        if room in booking_data:
            report_df = report_df.append({"Room": room, "Booking Status": booking_data[room]}, ignore_index=True)
        else:
            report_df = report_df.append({"Room": room, "Booking Status": "Not Listed"}, ignore_index=True)

    # Visualize report
    ax = report_df.plot.bar(x="Room", y="Booking Status", rot=0, figsize=(10, 5), fontsize=12)
    ax.set_xlabel("Room", fontsize=12)
    ax.set_ylabel("Booking Status", fontsize=12)
    ax.set_title("Booking Status Report for " + date_str, fontsize=14)
    ax.tick_params(axis="both", which="major", labelsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    return report_df, ax