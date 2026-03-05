
import pandas as pd
import time
OUTPUT_DIR = './output'
def task_func(df: pd.DataFrame, filename: str) -> str:
    """
    Write a Pandas DataFrame into a JSON Lines file and save it in a specified directory.
    :param df: The Pandas DataFrame to be written.
    :param filename: The name of the JSON Lines file to be saved.
    :return: The full path where the JSON Lines file was saved.
    """
    start_time = time.time()
    df.to_json(f'{OUTPUT_DIR}/{filename}.jsonl', orient='records')
    end_time = time.time()
    print(f'JSON Lines file saved in {OUTPUT_DIR}/{filename}.jsonl in {end_time - start_time} seconds')
    return f'{OUTPUT_DIR}/{filename}.jsonl'