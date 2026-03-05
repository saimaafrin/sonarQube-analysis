
import pandas as pd
import json
import os
import math

def task_func(json_data, output_dir=".", file_name="country_population_report.csv"):
    # Check if the JSON data is empty
    if not json_data:
        raise ValueError("The JSON data is empty.")
    
    # Initialize an empty list to store the data
    data = []
    
    # Iterate over the items in the JSON data
    for country, population in json_data.items():
        # Check if the country name is a string
        if not isinstance(country, str):
            raise ValueError("Non-string country name encountered.")
        
        # Check if the population is a number and non-negative
        if not isinstance(population, (int, float)) or population < 0:
            raise ValueError("Non-numeric or negative population encountered.")
        
        # Round down the population to the nearest integer if it's a float
        population = math.floor(population)
        
        # Append the data to the list
        data.append({"Country": country, "Population": population})
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the file path
    file_path = os.path.join(output_dir, file_name)
    
    # Write the DataFrame to a CSV file
    try:
        df.to_csv(file_path, index=False)
    except IOError as e:
        raise IOError(f"Failed to write to the specified directory: {e}")
    
    # Return the file path and the DataFrame
    return file_path, df