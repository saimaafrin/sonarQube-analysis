
import struct
import io
import gzip

def task_func(newArray):
    # Compress the array using gzip
    compressed_data = gzip.compress(struct.pack('d', newArray))
    return compressed_data