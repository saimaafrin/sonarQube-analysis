import json
import base64
import unicodedata
def task_func(json_file: str) -> dict:
    # Initialize an empty dictionary to store the results
    result = {}
    
    # Open and read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Iterate over each key-value pair in the JSON data
    for key, value in data.items():
        # Decode the base64 encoded string
        decoded_string = base64.b64decode(value).decode('utf-8')
        
        # Apply Unicode normalization form C (NFC)
        normalized_string = unicodedata.normalize('NFC', decoded_string)
        
        # Store the result in the dictionary
        result[key] = normalized_string
    
    # Return the dictionary containing the normalized, decoded strings
    return result