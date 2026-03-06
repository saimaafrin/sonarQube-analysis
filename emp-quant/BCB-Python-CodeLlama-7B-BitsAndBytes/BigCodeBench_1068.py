
import warnings
import sqlite3
import pandas as pd

def task_func(db_path, query, warn_large_dataset=True):
    """
    Fetches data from an SQLite database using the provided database path and SQL query.

    Parameters
    ----------
    db_path : str
        Path to the SQLite database file.
    query : str
        SQL query to execute on the database.
    warn_large_dataset : bool, optional
        Whether to warn the user if the data contains more than 10000 rows.
        Defaults to True.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the data fetched from the database.

    Raises
    ------
    Exception
        If any error occurs during database connection, SQL query execution, or data fetching.
        The error message provides details about the issue, starting with "Error fetching data from the database: ".
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)

        # Execute the SQL query
        cursor = conn.cursor()
        cursor.execute(query)

        # Fetch the data
        data = cursor.fetchall()

        # Convert the data to a DataFrame
        df = pd.DataFrame(data)

        # Check if the data contains more than 10000 rows
        if len(df) > 10000 and warn_large_dataset:
            warnings.warn("The data contains more than 10000 rows.")

        # Close the database connection
        conn.close()

        return df

    except Exception as e:
        # Raise an exception with a custom error message
        raise Exception(f"Error fetching data from the database: {e}")