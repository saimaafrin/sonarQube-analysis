
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
        table = tree.xpath('//table')[0]  # Assuming the first table is the one we want

        # Convert the table to a pandas DataFrame
        df = pd.read_html(html.tostring(table))[0]

        # Connect to the SQLite database
        conn = sqlite3.connect(database_name)

        # Replace the existing table with the new data
        df.to_sql('my_table', conn, if_exists='replace', index=False)

        # Close the database connection
        conn.close()

        # Return the number of rows in the parsed HTML table
        return len(df)

    except requests.RequestException as e:
        print(f"Network error: {e}")
        return 0

    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return 0

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0