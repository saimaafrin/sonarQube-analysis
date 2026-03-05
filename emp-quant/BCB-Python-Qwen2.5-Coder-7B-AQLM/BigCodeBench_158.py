
import json
import urllib.request
import urllib.parse
import gzip

def task_func(url_str, file_path):
    # Fetch the JSON data from the given URL
    response = urllib.request.urlopen(url_str)
    json_data = response.read()

    # Decode the JSON data
    decoded_data = json.loads(json_data)

    # Compress the decoded JSON data into a gzip file
    with gzip.open(file_path, 'wb') as f_out:
        f_out.write(json.dumps(decoded_data).encode('utf-8'))

    # Return the path to the compressed gzip file
    return file_path