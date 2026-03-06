
import requests
from lxml import html
import pandas as pd
import sqlite3

def task_func(webpage_url: str, database_name: str = "my_database.db") -> int:
    try:
        # Fetch the webpage content
        response = requests.get(webpage_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        tree = html.fromstring(response.content)

        # Extract the table data
        table_data = tree.xpath('//table//tr')
        if not table_data:
            return 0  # No table found

        # Convert the table data to a DataFrame
        headers = [header.text_content() for header in table_data[0]]
        rows = [[cell.text_content() for cell in row] for row in table_data[1:]]
        df = pd.DataFrame(rows, columns=headers)

        # Connect to the SQLite database
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # Drop the existing table if it exists
        cursor.execute("DROP TABLE IF EXISTS my_table")

        # Create a new table with the same structure as the DataFrame
        create_table_query = f"CREATE TABLE my_table ({', '.join([f'{col} TEXT' for col in df.columns])})"
        cursor.execute(create_table_query)

        # Insert the DataFrame data into the table
        for _, row in df.iterrows():
            placeholders = ', '.join(['?' for _ in range(len(row))])
            insert_query = f"INSERT INTO my_table VALUES ({placeholders})"
            cursor.execute(insert_query, tuple(row))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Return the number of rows inserted
        return len(df)

    except requests.RequestException as e:
        print(f"Network error: {e}")
        return -1
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return -1