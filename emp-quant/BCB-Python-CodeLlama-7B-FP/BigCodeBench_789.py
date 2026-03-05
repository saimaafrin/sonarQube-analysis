import numpy as np
from sklearn.preprocessing import MinMaxScaler
ARRAY_LENGTH = 10
def task_func():
    # Generate a random array
    array = np.random.rand(ARRAY_LENGTH)

    # Apply min-max normalization
    scaler = MinMaxScaler()
    scaled_array = scaler.fit_transform(array)

    # Output
    print(scaled_array)