
import requests
from lxml import html
import pandas as pd
import sqlite3

def task_func(webpage_url: str, database_name: str = "my_database.db") -> int:
    # Fetch the HTML content from the URL
    try:
        response = requests.get(webpage_url)
        response.raise_for_status()  # Raises an exception for HTTP errors
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return 0

    # Parse the HTML content
    tree = html.fromstring(response.content)
    try:
        # Assuming the table is the first table in the HTML
        table = tree.xpath('//table[1]')
        if not table:
            return 0
    except Exception as e:
        print(f"Error parsing the HTML table: {e}")
        return 0

    # Convert the table to a pandas DataFrame
    df = pd.read_html(str(table))[0]

    # Connect to the SQLite database
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        # Replace the table in the database with the new data
        df.to_sql('my_table', conn, if_exists='replace', index=False)
        conn.commit()
    except sqlite3.DatabaseError as e:
        print(f"Error connecting to or writing to the database: {e}")
        return 0

    # Close the database connection
    conn.close()

    # Return the number of rows in the parsed HTML table
    return df.shape[0]