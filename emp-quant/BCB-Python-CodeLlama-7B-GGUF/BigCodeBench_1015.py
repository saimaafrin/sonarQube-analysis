
import requests
from lxml import html
import pandas as pd
import sqlite3

def task_func(webpage_url: str, database_name: str = "my_database.db") -> int:
    """
    Parses HTML table data from a specified URL or local file and stores it into an SQLite database.

    Parameters:
    webpage_url (str): The URL of the HTML page containing the table data.
    database_name (str, optional): The name of the SQLite database to store the parsed data. Defaults to "my_database.db".

    Returns:
    int: The number of rows in the parsed HTML table.

    Raises:
    requests.RequestException: If there is a network issue in accessing the URL.
    sqlite3.DatabaseError: If there is an issue connecting to, or writing to, the SQLite database.
    """
    # Fetch the HTML content from the URL
    try:
        response = requests.get(webpage_url)
    except requests.RequestException as e:
        raise e

    # Parse the HTML content using lxml
    try:
        tree = html.fromstring(response.content)
    except html.etree.ParseError as e:
        raise e

    # Find the table in the HTML content
    table = tree.cssselect("table")[0]

    # Convert the table to a Pandas DataFrame
    df = pd.read_html(table)[0]

    # Connect to the SQLite database
    try:
        conn = sqlite3.connect(database_name)
    except sqlite3.DatabaseError as e:
        raise e

    # Create a new table in the SQLite database
    try:
        conn.execute("CREATE TABLE my_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    except sqlite3.DatabaseError as e:
        raise e

    # Insert the data from the Pandas DataFrame into the SQLite database
    try:
        conn.executemany("INSERT INTO my_table (name, age) VALUES (?, ?)", df.to_records(index=False))
    except sqlite3.DatabaseError as e:
        raise e

    # Commit the changes to the SQLite database
    conn.commit()

    # Close the SQLite connection
    conn.close()

    # Return the number of rows in the parsed HTML table
    return len(df)