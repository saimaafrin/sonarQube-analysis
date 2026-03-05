
import json
import urllib.request
import urllib.parse
import gzip

def task_func(url_str, file_path):
    # Fetch the JSON data from the given URL
    with urllib.request.urlopen(url_str) as response:
        data = response.read()

    # Decode the JSON data
    json_data = json.loads(data)

    # Compress the JSON data into a gzip file
    with gzip.open(file_path, 'wb') as f:
        f.write(json_data.encode())

    return file_path