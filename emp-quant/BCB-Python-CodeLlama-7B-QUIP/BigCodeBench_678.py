
import pandas as pd
import json
import os
import shutil

def task_func(path):
    # Create the "processed" subdirectory if it doesn't already exist
    if not os.path.exists(os.path.join(path, "processed")):
        os.makedirs(os.path.join(path, "processed"))

    # Read all JSON files in the directory and create a DataFrame
    df = pd.DataFrame()
    for file in os.listdir(path):
        if file.endswith(".json"):
            with open(os.path.join(path, file), "r") as f:
                data = json.load(f)
                df = df.append(pd.DataFrame(data))

    # Add a "Source" column to the DataFrame
    df["Source"] = file

    # Move the processed files to the "processed" subdirectory
    for file in os.listdir(path):
        if file.endswith(".json"):
            shutil.move(os.path.join(path, file), os.path.join(path, "processed", file))

    return df