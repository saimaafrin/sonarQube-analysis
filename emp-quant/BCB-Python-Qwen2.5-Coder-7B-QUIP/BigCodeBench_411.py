
import pandas as pd
import json

def task_func(data: dict, output_path: str = "./default_data_output.json") -> str:
    # Create a DataFrame from the input dictionary
    df = pd.DataFrame(data)
    
    # Drop the column named 'c' if it exists
    if 'c' in df.columns:
        df = df.drop(columns=['c'])
    
    # Convert the DataFrame to a dictionary
    data_dict = df.to_dict(orient='records')
    
    # Save the dictionary as a JSON file
    with open(output_path, 'w') as f:
        json.dump(data_dict, f)
    
    # Return the path where the JSON file was saved
    return output_path