
import pickle
import os

def task_func(df, file_name="save.pkl"):
    # Save the DataFrame to a pickle file
    with open(file_name, "wb") as f:
        pickle.dump(df, f)

    # Read the pickle file back into a DataFrame
    with open(file_name, "rb") as f:
        loaded_df = pickle.load(f)

    # Delete the intermediate file
    os.remove(file_name)

    return loaded_df