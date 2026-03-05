import requests
from lxml import html
import pandas as pd
import sqlite3
def task_func(webpage_url: str, database_name: str = "my_database.db") -> int:
    """
    Parses HTML table data from a specified URL or local file and stores it into an SQLite database.
    The function handles different scenarios for fetching, processing, and storing data.
    """
    # Fetch HTML content from the specified URL or local file
    try:
        response = requests.get(webpage_url)
    except requests.RequestException as e:
        raise e

    # Parse HTML content using lxml
    try:
        tree = html.fromstring(response.content)
    except html.etree.ParseError as e:
        raise e

    # Extract table data from HTML content
    try:
        table = tree.xpath('//table')
    except html.etree.XPathError as e:
        raise e

    # Convert table data to a Pandas DataFrame
    try:
        df = pd.read_html(table)[0]
    except pd.errors.EmptyDataError as e:
        raise e

    # Connect to the SQLite database
    try:
        conn = sqlite3.connect(database_name)
    except sqlite3.DatabaseError as e:
        raise e

    # Replace the table "my_table" in the specified SQLite database with new data
    try:
        df.to_sql("my_table", conn, if_exists="replace", index=False)
    except sqlite3.DatabaseError as e:
        raise e

    # Close the SQLite connection
    conn.close()

    # Return the number of rows in the parsed HTML table
    return df.shape[0]