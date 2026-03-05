
import time
import matplotlib.pyplot as plt

def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    try:
        seconds_list = []
        for time_str in time_strings:
            parsed_time = time.strptime(time_str, time_format)
            seconds = parsed_time.tm_sec
            seconds_list.append(seconds)
        
        fig, ax = plt.subplots()
        ax.hist(seconds_list, bins=60, range=(0, 60), edgecolor='black')
        ax.set_xlabel('Seconds')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram of Seconds Component')
        plt.show()
        
        return ax
    except ValueError as e:
        print(f"Error parsing time strings: {e}")
        return None