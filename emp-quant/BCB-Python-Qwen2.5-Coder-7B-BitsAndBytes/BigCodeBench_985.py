
import pandas as pd
import json
import os
import math

def task_func(json_data, output_dir=".", file_name="country_population_report.csv"):
    # Check if JSON data is empty
    if not json_data:
        raise ValueError("JSON data is empty")
    
    # Load JSON data into a dictionary
    try:
        data = json.loads(json_data)
    except json.JSONDecodeError:
        raise ValueError("Malformed JSON data")
    
    # Initialize an empty list to store the processed data
    processed_data = []
    
    # Process each item in the JSON data
    for item in data:
        country = item.get('country')
        population = item.get('population')
        
        # Validate country name
        if not isinstance(country, str):
            raise ValueError("Non-string country name encountered")
        
        # Validate population
        if not isinstance(population, (int, float)) or population < 0:
            raise ValueError("Non-numeric or negative population encountered")
        
        # Round down to the nearest integer if population is a float
        if isinstance(population, float):
            population = math.floor(population)
        
        # Append the validated data to the list
        processed_data.append({'Country': country, 'Population': population})
    
    # Create a DataFrame from the processed data
    df = pd.DataFrame(processed_data)
    
    # Ensure there's no extra index column
    df.reset_index(drop=True, inplace=True)
    
    # Define the output file path
    output_file_path = os.path.join(output_dir, file_name)
    
    # Write the DataFrame to a CSV file
    try:
        df.to_csv(output_file_path, index=False)
    except IOError:
        raise IOError(f"Cannot write to the specified directory: {output_dir}")
    
    # Return the file path and the DataFrame
    return output_file_path, df