
import json
import urllib.request
import urllib.parse
import gzip

def task_func(url_str, file_path):
    # Fetch JSON data from the given URL
    response = urllib.request.urlopen(url_str)
    json_data = response.read()
    
    # Decode the JSON data
    decoded_json = json.loads(json_data.decode('utf-8'))
    
    # Compress the JSON data into a gzip file
    with open(file_path, 'wb') as f_out:
        with gzip.GzipFile(fileobj=f_out) as f_gz:
            f_gz.write(json.dumps(decoded_json).encode('utf-8'))
    
    return file_path