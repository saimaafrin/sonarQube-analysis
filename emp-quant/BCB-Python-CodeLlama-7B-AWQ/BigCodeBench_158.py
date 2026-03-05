import json
import urllib.request
import urllib.parse
import gzip
def task_func(url_str, file_path):
    """
    Fetches JSON data from a given URL, decodes the json-formatted data, and compresses it into a gzip file.
    The function should output with:
        str: The path to the compressed gzip file containing the JSON data.
    """
    # Fetch JSON data from the given URL
    response = urllib.request.urlopen(url_str)
    data = response.read()

    # Decode the JSON data
    json_data = json.loads(data)

    # Compress the JSON data into a gzip file
    with gzip.open(file_path, 'wb') as f:
        f.write(json.dumps(json_data).encode('utf-8'))

    # Return the path to the compressed gzip file
    return file_path
url_str = "https://jsonplaceholder.typicode.com/posts"
file_path = "posts.json.gz"