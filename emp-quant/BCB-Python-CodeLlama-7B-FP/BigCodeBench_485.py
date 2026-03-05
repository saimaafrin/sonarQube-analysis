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
    utc_diff = np.zeros(end_date - start_date)
    los_angeles_diff = np.zeros(end_date - start_date)
    paris_diff = np.zeros(end_date - start_date)
    kolkata_diff = np.zeros(end_date - start_date)
    sydney_diff = np.zeros(end_date - start_date)

    # Calculate time differences
    for i in range(start_date, end_date):
        utc_diff[i - start_date] = utc.localize(i).utcoffset().total_seconds() / 3600
        los_angeles_diff[i - start_date] = los_angeles.localize(i).utcoffset().total_seconds() / 3600
        paris_diff[i - start_date] = paris.localize(i).utcoffset().total_seconds() / 3600
        kolkata_diff[i - start_date] = kolkata.localize(i).utcoffset().total_seconds() / 3600
        sydney_diff[i - start_date] = sydney.localize(i).utcoffset().total_seconds() / 3600

    # Plot time differences
    fig, ax = plt.subplots()
    ax.plot(utc_diff, label='UTC', color='b')
    ax.plot(los_angeles_diff, label='America/Los_Angeles', color='g')
    ax.plot(paris_diff, label='Europe/Paris', color='r')
    ax.plot(kolkata_diff, label='Asia/Kolkata', color='c')
    ax.plot(sydney_diff, label='Australia/Sydney', color='m')
    ax.set_xlabel('Hour')
    ax.set_ylabel('Time difference (hours)')
    ax.set_title('Time differences between UTC and predefined time zones')
    ax.legend()
    return ax
start_time = '2022-01-01 00:00:00'
end_time = '2022-01-02 00:00:00'