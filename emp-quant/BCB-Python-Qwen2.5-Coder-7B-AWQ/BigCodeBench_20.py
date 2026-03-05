import ast
import pandas as pd
import seaborn as sns
def task_func(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Convert the string representations of dictionaries in 'dict_column' to actual Python dictionaries
    df['dict_column'] = df['dict_column'].apply(ast.literal_eval)
    
    # Create a PairGrid object using Seaborn's pairplot
    ax = sns.pairplot(df)
    
    # Return the DataFrame and the PairGrid object as a tuple
    return df, ax