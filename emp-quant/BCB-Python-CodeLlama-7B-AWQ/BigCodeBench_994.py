import requests
import pandas as pd
from bs4 import BeautifulSoup
def task_func(url: str, csv_file_path: str) -> list:
    """
    Extracts title, date, and author information from a webpage and writes the data to a CSV file.
    The function iterates through each 'div' element with a class 'container', extracting the text of 'h1', and 'span' elements with classes 'date' and 'author', respectively.
    Default values ('No Title', 'No Date', or 'No Author') are used if an element is not found.
    The extracted data is stored in a list of tuples. The list of tuples is then converted into a Pandas DataFrame and saved to a CSV file at the specified file path.
    The DataFrame's columns are labeled as 'Title', 'Date', and 'Author'.
    The function returns the list of tuples.
    """
    try:
        # Make an HTTP request to the specified URL
        response = requests.get(url, timeout=5)
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract the title, date, and author information
        title = soup.find('h1', class_='container').text.strip() or 'No Title'
        date = soup.find('span', class_='date').text.strip() or 'No Date'
        author = soup.find('span', class_='author').text.strip() or 'No Author'
        # Create a list of tuples with the extracted data
        data = [(title, date, author)]
        # Convert the list of tuples to a Pandas DataFrame
        df = pd.DataFrame(data, columns=['Title', 'Date', 'Author'])
        # Save the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False)
        return data
    except requests.RequestException as e:
        # Raise a RuntimeError with a message that includes the details of the exception
        raise RuntimeError(f'Error fetching URL: {e}')
url = 'https://www.example.com'
csv_file_path = 'output.csv'