from sklearn.preprocessing import StandardScaler
import numpy as np
import base64
def task_func(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    scaled_data_base64 = base64.b64encode(scaled_data)
    return scaled_data_base64.decode("ascii")
data = np.array([1, 2, 3, 4, 5])