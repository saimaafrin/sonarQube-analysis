
import sqlite3
import pandas as pd
import seaborn as sns

def task_func(db_name="test.db", table_name="People"):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    # Load data from the table into a pandas DataFrame
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    
    # Check for negative age values
    if df['age'].min() < 0:
        raise ValueError("Data contains negative age values")
    
    # Draw the age distribution plot
    ax = sns.histplot(df['age'], kde=True, bins=30)
    
    # Return the Axes object
    return ax