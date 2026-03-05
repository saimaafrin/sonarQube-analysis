
import json
import urllib.request
import urllib.parse
import gzip

def task_func(url_str, file_path):
    # Fetch JSON data from the given URL
    response = urllib.request.urlopen(url_str)
    data = response.read()

    # Decode the JSON data
    json_data = json.loads(data)

    # Compress the JSON data into a gzip file
    with gzip.open(file_path, 'wb') as f:
        f.write(json_data)

    # Return the path to the compressed gzip file
    return file_path