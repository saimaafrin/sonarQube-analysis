from datetime import datetime
import pandas as pd
import pytz
import matplotlib.pyplot as plt
TIMEZONES = [
    "America/New_York",
    "Europe/London",
    "Asia/Shanghai",
    "Asia/Tokyo",
    "Australia/Sydney",
]
def task_func(timestamp):
    """
    Convert a Unix timestamp to date objects in different time zones, create a Pandas DataFrame, and draw a bar chart.
    - You should use the time zones mentionned in the constant TIMEZONES.
    - The date format should be as DATE_FORMAT.
    - The DataFrame should have 'Timezone' and 'Datetime' as column names.
    - The x-label of the bar plot should be set to 'Timezone' while the y-label should be set to 'Datetime'.
    - The plot title should be "Datetime = f(Timezone)"

    Parameters:
    timestamp (int): The Unix timestamp.

    Returns:
    tuple: A tuple containing:
        - DataFrame: A pandas DataFrame containing the datetime in different timezones.
        - Axes: A matplotlib Axes object for the generated bar chart.

    Requirements:
    - datetime
    - pandas
    - pytz
    - matplotlib.pyplot

    Example:
    >>> df, ax = task_func(1347517370)
    >>> print(df)
               Timezone            Datetime
    0  America/New_York 2012-09-13 02:22:50
    1     Europe/London 2012-09-13 07:22:50
    2     Asia/Shanghai 2012-09-13 14:22:50
    3        Asia/Tokyo 2012-09-13 15:22:50
    4  Australia/Sydney 2012-09-13 16:22:50
    """
    # Convert the Unix timestamp to a datetime object
    dt = datetime.fromtimestamp(timestamp)

    # Create a list of datetime objects in different timezones
    timezones = []
    for tz in TIMEZONES:
        timezones.append(pytz.timezone(tz).localize(dt))

    # Create a DataFrame with the timezones and the datetime objects
    df = pd.DataFrame(timezones, columns=["Timezone", "Datetime"])

    # Draw a bar chart
    ax = df.plot(kind="bar", x="Timezone", y="Datetime", rot=0)

    # Set the x-label and the y-label
    ax.set_xlabel("Timezone")
    ax.set_ylabel("Datetime")

    # Set the plot title
    ax.set_title("Datetime = f(Timezone)")

    return df, ax