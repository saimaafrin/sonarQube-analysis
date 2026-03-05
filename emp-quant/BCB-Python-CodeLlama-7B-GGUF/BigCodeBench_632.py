
import pandas as pd
import time
OUTPUT_DIR = './output'
def task_func(df: pd.DataFrame, filename: str) -> str:
    # Save the DataFrame to a JSON Lines file
    df.to_json(OUTPUT_DIR + '/' + filename + '.jsonl', orient='records')
    # Return the full path where the JSON Lines file was saved
    return OUTPUT_DIR + '/' + filename + '.jsonl'