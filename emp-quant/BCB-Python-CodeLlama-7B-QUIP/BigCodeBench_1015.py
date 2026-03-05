
import requests
from lxml import html
import pandas as pd
import sqlite3

def task_func(webpage_url: str, database_name: str = "my_database.db") -> int:
    try:
        # Fetch the HTML content from the specified URL
        response = requests.get(webpage_url)
        if response.status_code == 200:
            # Parse the HTML content using the lxml library
            html_content = html.fromstring(response.content)
            # Find the table in the HTML content
            table_element = html_content.xpath("//table")[0]
            # Convert the table to a pandas DataFrame
            table_data = pd.DataFrame(table_element.text.split("\n"))
            # Connect to the SQLite database
            conn = sqlite3.connect(database_name)
            # Clear the existing table data
            conn.execute("DELETE FROM my_table")
            # Insert the new table data
            conn.execute("INSERT INTO my_table VALUES (?, ?, ?)", (table_data.values.tolist()))
            # Commit the changes to the database
            conn.commit()
            # Close the database connection
            conn.close()
            # Return the number of rows in the parsed HTML table
            return table_data.shape[0]
        else:
            return 0
    except requests.RequestException as e:
        raise e
    except sqlite3.DatabaseError as e:
        raise e