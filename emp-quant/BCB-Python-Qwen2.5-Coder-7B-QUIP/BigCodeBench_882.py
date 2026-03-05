
import sqlite3
import pandas as pd
import os

def task_func(db_file, table_name, column_name, pattern='\d+[xX]'):
    # Check if the database file exists
    if not os.path.exists(db_file):
        raise ValueError("Database file does not exist.")

    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)

    # Query the table
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    # Find matches using regex
    df['matches'] = df[column_name].apply(lambda x: re.findall(pattern, x))

    # Return the DataFrame with matches
    return df