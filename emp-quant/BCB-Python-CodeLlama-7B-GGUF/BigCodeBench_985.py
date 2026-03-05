
import pandas as pd
import json
import os
import math

def task_func(json_data, output_dir=".", file_name="country_population_report.csv"):
    # Load JSON data into a dictionary
    data = json.loads(json_data)

    # Check if the JSON data is malformed or empty
    if not data or not isinstance(data, dict):
        raise ValueError("Malformed JSON data")

    # Check if the JSON data contains non-string country names
    if not all(isinstance(country, str) for country in data.keys()):
        raise ValueError("Non-string country names in JSON data")

    # Check if the JSON data contains non-numeric or negative populations
    if not all(isinstance(population, (int, float)) and population >= 0 for population in data.values()):
        raise ValueError("Non-numeric or negative population in JSON data")

    # Create a DataFrame with the country-population data
    df = pd.DataFrame(data, columns=["Country", "Population"])

    # Round down float populations to the nearest integer
    df["Population"] = df["Population"].apply(lambda x: math.floor(x) if isinstance(x, float) else x)

    # Remove extra index column
    df.reset_index(drop=True, inplace=True)

    # Save DataFrame to CSV file
    file_path = os.path.join(output_dir, file_name)
    df.to_csv(file_path, index=False)

    # Return file path and DataFrame
    return file_path, df