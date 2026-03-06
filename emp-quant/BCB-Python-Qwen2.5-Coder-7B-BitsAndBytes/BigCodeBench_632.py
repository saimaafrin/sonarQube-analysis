
import pandas as pd
import time
from pathlib import Path

OUTPUT_DIR = './output'

def task_func(df: pd.DataFrame, filename: str) -> str:
    # Ensure the output directory exists
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    
    # Create the full path for the JSON Lines file
    filepath = Path(OUTPUT_DIR) / f"{filename}.jsonl"
    
    # Write the DataFrame to a JSON Lines file
    df.to_json(filepath, orient='records', lines=True)
    
    # Return the full path where the JSON Lines file was saved
    return str(filepath)