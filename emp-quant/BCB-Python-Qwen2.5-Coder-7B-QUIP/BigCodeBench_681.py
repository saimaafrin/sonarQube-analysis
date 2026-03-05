
import pandas as pd
import json

def task_func(file_path, key):
    # Load the JSON file into a Pandas DataFrame
    df = pd.read_json(file_path)
    
    # Remove the specific key from each object
    df = df.drop(columns=[key])
    
    # Write the processed DataFrame back into a JSON file oriented by records
    df.to_json(file_path, orient='records')
    
    # Return the processed DataFrame
    return df