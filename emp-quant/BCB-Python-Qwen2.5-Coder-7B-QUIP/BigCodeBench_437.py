
import pickle
import os
def task_func(df, file_name="save.pkl"):
    # Save the DataFrame to a pickle file
    df.to_pickle(file_name)
    
    # Load the DataFrame from the pickle file
    loaded_df = pd.read_pickle(file_name)
    
    # Delete the intermediate pickle file
    os.remove(file_name)
    
    return loaded_df