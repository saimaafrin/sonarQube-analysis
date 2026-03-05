import pandas as pd
import json
def task_func(file_path, key):
    # Load the JSON file into a Pandas DataFrame
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Convert the list of dictionaries into a DataFrame
    df = pd.DataFrame(data)
    
    # Remove the specified key from each dictionary in the DataFrame
    df = df.drop(columns=[key])
    
    # Write the processed DataFrame back into a JSON file oriented by records
    df.to_json('processed_data.json', orient='records', lines=True)
    
    return df