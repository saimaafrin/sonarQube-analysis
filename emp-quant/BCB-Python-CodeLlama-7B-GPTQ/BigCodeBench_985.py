import pandas as pd
import json
import os
import math
def task_func(json_data, output_dir=".", file_name="country_population_report.csv"):
    """
    Generates a population report DataFrame and CSV file based on provided JSON data.

    Args:
        json_data (str): JSON data containing country-population data.
        output_dir (str, optional): Directory to write the CSV file to. Defaults to ".".
        file_name (str, optional): Name of the CSV file to write. Defaults to "country_population_report.csv".

    Returns:
        str: The file path of the generated CSV report.
        pd.DataFrame: The country-population data loaded from the input JSON, with columns:
            "Country", "Population".

    Raises:
        ValueError: If the JSON data is malformed, empty, contains non-string country names, non-numeric or negative populations.
        IOError: If the file cannot be written to the specified directory.
    """
    # Load JSON data into a dictionary
    data = json.loads(json_data)

    # Check if the JSON data is empty or malformed
    if not data or not isinstance(data, dict):
        raise ValueError("Invalid JSON data")

    # Check if the JSON data contains non-string country names
    if not all(isinstance(country, str) for country in data.keys()):
        raise ValueError("Non-string country names in JSON data")

    # Check if the JSON data contains non-numeric or negative populations
    if not all(isinstance(population, (int, float)) and population >= 0 for population in data.values()):
        raise ValueError("Non-numeric or negative population in JSON data")

    # Create a DataFrame with the country-population data
    df = pd.DataFrame(data, columns=["Country", "Population"])

    # Round down float populations to the nearest integer
    df["Population"] = df["Population"].apply(lambda x: math.floor(x))

    # Write the DataFrame to a CSV file
    file_path = os.path.join(output_dir, file_name)
    df.to_csv(file_path, index=False)

    return file_path, df
json_data = '{"USA": 331410000, "China": 1439323666, "India": 1380000000}'
output_dir = "."
file_name = "country_population_report.csv"