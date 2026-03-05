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
    # Load JSON data into a pandas DataFrame
    df = pd.read_json(json_data)

    # Check for malformed or empty JSON data
    if df.empty:
        raise ValueError("JSON data is empty or malformed")

    # Check for non-string country names
    if not df["Country"].apply(lambda x: isinstance(x, str)).all():
        raise ValueError("JSON data contains non-string country names")

    # Check for non-numeric or negative populations
    if not df["Population"].apply(lambda x: isinstance(x, (int, float)) and x >= 0).all():
        raise ValueError("JSON data contains non-numeric or negative populations")

    # Round down float populations to the nearest integer
    df["Population"] = df["Population"].apply(lambda x: math.floor(x) if isinstance(x, float) else x)

    # Write CSV file to output directory
    file_path = os.path.join(output_dir, file_name)
    df.to_csv(file_path, index=False)

    return file_path, df
json_data = '{"countries": [{"country": "USA", "population": 331000000}, {"country": "China", "population": 1400000000}, {"country": "India", "population": 13600000000}, {"country": "Japan", "population": 1260000000}]}'
output_dir = "."
file_name = "country_population_report.csv"