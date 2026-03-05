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
        table = tree.xpath('//table')[0]
        rows = table.xpath('.//tr')
        data = []

        for row in rows:
            cols = row.xpath('.//td')
            cols = [col.text.strip() for col in cols]
            data.append(cols)

        # Create a DataFrame from the table data
        df = pd.DataFrame(data[1:], columns=data[0])

        # Connect to the SQLite database
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # Drop the existing table if it exists
        cursor.execute("DROP TABLE IF EXISTS my_table")

        # Create a new table
        df.to_sql('my_table', conn, if_exists='replace', index=False)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Return the number of rows in the parsed HTML table
        return len(df)

    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return 0

    except sqlite3.DatabaseError as e:
        print(f"Error connecting to or writing to the database: {e}")
        return 0

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0