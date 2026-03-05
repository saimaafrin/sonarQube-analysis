import numpy as np
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(data_dict):
    # Add key "a" with a value of 1
    data_dict["a"] = 1
    
    # Convert dictionary values to a numpy array
    values = np.array(list(data_dict.values()))
    
    # Calculate mean, median, and mode
    mean = round(np.mean(values), 2)
    median = np.median(values)
    mode = stats.mode(values)[0][0]
    
    # Create a dictionary for statistical properties
    stats_dict = {
        "mean": mean,
        "median": median,
        "mode": mode
    }
    
    # Initialize MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Normalize the values
    normalized_values = scaler.fit_transform(values.reshape(-1, 1)).flatten()
    
    # Plot histogram of normalized values
    plt.figure()
    histogram = plt.hist(normalized_values, bins=10, edgecolor='black')
    plt.title("Histogram of Normalized Values")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    
    # Return the processed dictionary, statistical properties, and histogram plot
    return data_dict, stats_dict, histogram