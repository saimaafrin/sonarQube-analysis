import pickle
import os
def task_func(df, file_name="save.pkl"):
    """
    Save the provided Pandas DataFrame 'df' in a pickle file with the given name,
    read it back for validation, and delete the intermediate file.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame to be saved.
    - file_name (str): The name of the pickle file to save the DataFrame.
    
    Returns:
    - loaded_df (pd.DataFrame): The loaded DataFrame from the specified file.
    """
    # Save the DataFrame to a pickle file
    df.to_pickle(file_name)
    
    # Read the DataFrame back from the pickle file
    loaded_df = pd.read_pickle(file_name)
    
    # Delete the intermediate pickle file
    os.remove(file_name)
    
    return loaded_df