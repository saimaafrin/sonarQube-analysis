import requests
from lxml import html
import pandas as pd
import sqlite3
def task_func(webpage_url: str, database_name: str = "my_database.db") -> int:
    try:
        # Fetch the HTML content from the webpage
        response = requests.get(webpage_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        tree = html.fromstring(response.content)

        # Extract the table data
        table = tree.xpath('//table')
        if not table:
            return 0  # No table found

        # Convert the table to a pandas DataFrame
        df = pd.read_html(str(table[0]))[0]

        # Connect to the SQLite database
        conn = sqlite3.connect(database_name)

        # Replace the table in the database with the new data
        df.to_sql('my_table', conn, if_exists='replace', index=False)

        # Close the database connection
        conn.close()

        # Return the number of rows in the parsed HTML table
        return len(df)

    except requests.RequestException as e:
        raise e  # Raise the exception for network issues
    except sqlite3.DatabaseError as e:
        raise e  # Raise the exception for database issues