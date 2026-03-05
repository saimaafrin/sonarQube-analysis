
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def task_func(db_name, table_name):
    # Connect to the database
    conn = sqlite3.connect(db_name)

    # Query the table
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)

    # Exclude the 'id' column
    df = df.drop(columns=['id'])

    # Check if the table has less than two numerical columns
    if len(df.select_dtypes(include=[np.number]).columns) < 2:
        raise ValueError("ValueError: If the table has less than two numerical columns.")

    # Plot the relationship between the first and second numerical columns
    plt.scatter(df.iloc[:, 0], df.iloc[:, 1])
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.title(f"Scatterplot of {table_name}")
    plt.show()

    # Close the connection
    conn.close()