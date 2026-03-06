
import requests
from lxml import html
import pandas as pd
import sqlite3

def task_func(webpage_url: str, database_name: str = "my_database.db") -> int:
    """
    Parses HTML table data from a specified URL or local file and stores it into an SQLite database.

    Parameters:
        webpage_url (str): The URL of the webpage to parse.
        database_name (str, optional): The name of the SQLite database to store the parsed data. Defaults to "my_database.db".

    Returns:
        int: The number of rows in the parsed HTML table.

    Raises:
        requests.RequestException: If there is a network issue in accessing the URL.
        sqlite3.DatabaseError: If there is an issue connecting to, or writing to, the SQLite database.
    """
    # Fetch the HTML content from the webpage
    try:
        response = requests.get(webpage_url)
    except requests.RequestException as e:
        raise e

    # Parse the HTML content using lxml
    tree = html.fromstring(response.content)

    # Find the table in the HTML content
    table = tree.xpath('//table')

    # Check if the table exists and is not empty
    if not table or not table[0].xpath('tr'):
        return 0

    # Convert the table to a Pandas DataFrame
    df = pd.read_html(str(table))[0]

    # Connect to the SQLite database
    conn = sqlite3.connect(database_name)

    # Replace the existing table with the new data
    conn.execute("DROP TABLE IF EXISTS my_table")
    conn.execute("CREATE TABLE my_table (%s)" % ", ".join(df.columns))
    conn.executemany("INSERT INTO my_table VALUES (%s)" % ", ".join(["?"] * len(df.columns)), df.values)

    # Close the SQLite connection
    conn.close()

    # Return the number of rows in the parsed HTML table
    return len(df)