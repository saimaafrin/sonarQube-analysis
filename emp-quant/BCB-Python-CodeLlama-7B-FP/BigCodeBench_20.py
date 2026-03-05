import ast
import pandas as pd
import seaborn as sns
def task_func(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Convert the string representations of dictionaries in the 'dict_column' to Python dictionaries
    df['dict_column'] = df['dict_column'].apply(ast.literal_eval)

    # Visualize the data with Seaborn's pairplot
    ax = sns.pairplot(df, x_vars=['x1', 'x2'], y_vars=['y1', 'y2'], hue='dict_column')

    return df, ax
csv_file = 'data.csv'