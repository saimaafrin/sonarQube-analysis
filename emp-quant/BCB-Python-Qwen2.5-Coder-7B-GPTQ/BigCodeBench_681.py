import pandas as pd
import json
def task_func(file_path, key):
    # Load the JSON file into a DataFrame
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Convert the data into a DataFrame
    df = pd.DataFrame(data)
    
    # Remove the specified key from each object
    df = df.drop(columns=[key])
    
    # Write the processed DataFrame back into a JSON file oriented by records
    df.to_json('processed_data.json', orient='records')
    
    return df