
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Constants
ARRAY_LENGTH = 10

def task_func():
    # Generate a random array
    random_array = np.random.rand(ARRAY_LENGTH)

    # Apply min-max normalization
    scaler = MinMaxScaler()
    scaled_array = scaler.fit_transform(random_array)

    # Output the normalized array
    print(scaled_array)