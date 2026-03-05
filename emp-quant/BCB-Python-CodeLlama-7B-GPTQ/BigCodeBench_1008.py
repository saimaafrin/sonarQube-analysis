import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
def task_func(url, table_id):
    """
    Extracts and converts data from a specified HTML table based on the given 'table_id' on a webpage into a Pandas DataFrame.
    If the table is present but contains no data rows (i.e., no <tr> tags), the function returns an empty DataFrame.
    """
    try:
        # Send an HTTP request to the specified URL
        response = requests.get(url)

        # Check if the HTTP request was successful
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f"HTTP request failed with status code {response.status_code}")

        # Parse the HTML content of the webpage using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the table with the specified ID
        table = soup.find("table", {"id": table_id})

        # Check if the table was found
        if table is None:
            raise ValueError(f"Table with the specified ID '{table_id}' not found.")

        # Extract the data from the table
        data = []
        for row in table.find_all("tr"):
            row_data = []
            for cell in row.find_all("td"):
                row_data.append(cell.text.strip())
            data.append(row_data)

        # Create a Pandas DataFrame from the extracted data
        df = pd.DataFrame(data, columns=table.find_all("th"))

        # Return the DataFrame
        return df

    except requests.exceptions.HTTPError as e:
        raise e
    except ValueError as e:
        raise e
url = "https://example.com/data.html"
table_id = "my_table"