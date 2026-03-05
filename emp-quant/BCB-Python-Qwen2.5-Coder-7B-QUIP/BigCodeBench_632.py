
import pandas as pd
import time
OUTPUT_DIR = './output'

def task_func(df: pd.DataFrame, filename: str) -> str:
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Define the full path for the output file
    output_path = os.path.join(OUTPUT_DIR, filename)

    # Write the DataFrame to a JSON Lines file
    df.to_json(output_path, orient='records', lines=True)

    # Return the full path where the JSON Lines file was saved
    return output_path