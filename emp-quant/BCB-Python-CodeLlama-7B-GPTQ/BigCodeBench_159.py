import struct
import io
import gzip
def task_func(newArray):
    # Compress the NumPy array using gzip
    compressed_data = io.BytesIO()
    with gzip.GzipFile(fileobj=compressed_data, mode='wb') as f:
        f.write(struct.pack('d' * newArray.size, *newArray.flatten()))
    return compressed_data.getvalue()
newArray = np.array([1, 2, 3, 4, 5])