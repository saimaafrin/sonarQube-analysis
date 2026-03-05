
import bisect
import statistics
def task_func(df, column, value):
    if column not in df:
        raise ValueError("Column does not exist in DataFrame")
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number")
    avg = statistics.mean(df[column])
    greater_than_avg = df[column][df[column] > avg]
    count = len(greater_than_avg)
    hist, bin_edges = np.histogram(greater_than_avg, bins=50)
    ax = plt.axes()
    ax.hist(greater_than_avg, bins=50)
    return (hist, count, ax)