
import pandas as pd
import time
import json
import os

OUTPUT_DIR = './output'

def task_func(df: pd.DataFrame, filename: str) -> str:
    # Create the output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Convert the DataFrame to a JSON Lines file
    json_data = df.to_json(orient='records')

    # Save the JSON Lines file to the output directory
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(json_data)

    return filepath