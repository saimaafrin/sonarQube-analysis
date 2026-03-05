from datetime import datetime, timedelta
import pytz
import numpy as np
import matplotlib.pyplot as plt
def task_func(start_time, end_time):
    # Define time zones
    utc = pytz.timezone('UTC')
    los_angeles = pytz.timezone('America/Los_Angeles')
    paris = pytz.timezone('Europe/Paris')
    kolkata = pytz.timezone('Asia/Kolkata')
    sydney = pytz.timezone('Australia/Sydney')

    # Define time range
    start_date = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

    # Define time difference arrays
    utc_diff = []
    los_angeles_diff = []
    paris_diff = []
    kolkata_diff = []
    sydney_diff = []

    # Iterate over time range
    for date in np.arange(start_date, end_date, timedelta(hours=1)):
        # Convert date to UTC
        utc_date = utc.localize(date)

        # Calculate time difference for each time zone
        los_angeles_diff.append(los_angeles.localize(date).utcoffset(utc_date))
        paris_diff.append(paris.localize(date).utcoffset(utc_date))
        kolkata_diff.append(kolkata.localize(date).utcoffset(utc_date))
        sydney_diff.append(sydney.localize(date).utcoffset(utc_date))

    # Plot time differences
    fig, ax = plt.subplots()
    ax.plot(utc_diff, 'b', label='UTC')
    ax.plot(los_angeles_diff, 'g', label='America/Los_Angeles')
    ax.plot(paris_diff, 'r', label='Europe/Paris')
    ax.plot(kolkata_diff, 'c', label='Asia/Kolkata')
    ax.plot(sydney_diff, 'm', label='Australia/Sydney')
    ax.set_xlabel('Time')
    ax.set_ylabel('Time Difference (hours)')
    ax.set_title('Time Differences between UTC and Predefined Time Zones')
    ax.legend()
    return ax
start_time = '2022-01-01 00:00:00'
end_time = '2022-01-02 00:00:00'