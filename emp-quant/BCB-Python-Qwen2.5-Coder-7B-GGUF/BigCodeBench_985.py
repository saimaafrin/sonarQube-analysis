
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
    
    # Initialize a list to store country and population data
    country_population = []
    
    # Iterate through the JSON data
    for country, population in data.items():
        # Check if country name is a string
        if not isinstance(country, str):
            raise ValueError("Non-string country name encountered")
        
        # Check if population is numeric and non-negative
        if not isinstance(population, (int, float)) or population < 0:
            raise ValueError("Non-numeric or negative population encountered")
        
        # Round down to the nearest integer if population is a float
        population = math.floor(population)
        
        # Append the country and population to the list
        country_population.append([country, population])
    
    # Create a DataFrame from the list of country and population data
    df = pd.DataFrame(country_population, columns=["Country", "Population"])
    
    # Check if output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the file path for the CSV report
    file_path = os.path.join(output_dir, file_name)
    
    # Write the DataFrame to a CSV file
    try:
        df.to_csv(file_path, index=False)
    except IOError:
        raise IOError(f"Cannot write to the specified directory: {output_dir}")
    
    # Return the file path of the generated CSV report and the DataFrame
    return file_path, df