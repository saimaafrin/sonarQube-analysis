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
    
    # Initialize lists to store country names and populations
    countries = []
    populations = []
    
    # Iterate through the JSON data
    for item in data:
        # Check if the item is a dictionary and contains the required keys
        if not isinstance(item, dict) or "country" not in item or "population" not in item:
            raise ValueError("Invalid JSON data format")
        
        # Extract country name and population
        country = item["country"]
        population = item["population"]
        
        # Check if the country name is a string
        if not isinstance(country, str):
            raise ValueError("Non-string country name")
        
        # Check if the population is a non-negative integer
        if not isinstance(population, (int, float)) or population < 0:
            raise ValueError("Non-numeric or negative population")
        
        # Round down the population to the nearest integer
        population = math.floor(population)
        
        # Append the country and population to the lists
        countries.append(country)
        populations.append(population)
    
    # Create a DataFrame from the lists
    df = pd.DataFrame({"Country": countries, "Population": populations})
    
    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the file path
    file_path = os.path.join(output_dir, file_name)
    
    # Write the DataFrame to a CSV file
    try:
        df.to_csv(file_path, index=False)
    except IOError:
        raise IOError("Cannot write to the specified directory")
    
    # Return the file path and the DataFrame
    return file_path, df