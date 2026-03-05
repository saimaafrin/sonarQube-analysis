
import pandas as pd
import json
import os
import math

def task_func(json_data, output_dir=".", file_name="country_population_report.csv"):
    # Load JSON data
    try:
        data = json.loads(json_data)
    except json.JSONDecodeError:
        raise ValueError("Malformed JSON data")

    # Validate and clean data
    cleaned_data = []
    for item in data:
        if not isinstance(item, dict) or len(item) != 2:
            raise ValueError("Invalid data format")
        country, population = item["country"], item["population"]
        if not isinstance(country, str):
            raise ValueError("Non-string country name")
        if not isinstance(population, (int, float)) or population < 0:
            raise ValueError("Non-numeric or negative population")
        cleaned_data.append({"Country": country, "Population": int(math.floor(population))})

    # Create DataFrame
    df = pd.DataFrame(cleaned_data)

    # Write to CSV
    try:
        output_path = os.path.join(output_dir, file_name)
        df.to_csv(output_path, index=False)
    except IOError as e:
        raise IOError(f"Failed to write to file: {e}")

    return output_path, df