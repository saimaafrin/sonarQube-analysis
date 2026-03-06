import bs4
import requests
import re
import csv
def task_func(url="http://example.com", csv_path="emails.csv", 
          regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", 
          headers={'User-Agent': 'Mozilla/5.0'}):
    """
    Scrapes a web page to extract all email addresses using a specified regular expression pattern and writes them to a CSV file. The csv file is
    always created eventhough no email is found in the url. The header of the csv should be "Emails".

    Parameters:
    - url (str): The URL of the web page to scrape. Default is "http://example.com".
    - csv_path (str): The filesystem path where the CSV file should be saved. Default is "emails.csv".
    - regex (str): The regular expression pattern used to identify email addresses. Default is a pattern that matches common email formats.
    - headers (dict): The HTTP headers to use for the request. Default includes a User-Agent header.

    Returns:
    - str: The path to the CSV file where the extracted email addresses have been saved.

    Requirements:
    - bs4
    - requests
    - re
    - csv
    
    Examples:
    >>> task_func()
    'emails.csv'
    >>> task_func(url="http://another-example.com", csv_path="another_emails.csv")
    'another_emails.csv'
    """
    # Create the CSV file if it does not exist
    if not csv_path:
        csv_path = "emails.csv"
    with open(csv_path, "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Emails"])

    # Get the HTML page
    response = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # Find all email addresses
    emails = soup.find_all(text=re.compile(regex))

    # Write the email addresses to the CSV file
    with open(csv_path, "a") as csv_file:
        csv_writer = csv.writer(csv_file)
        for email in emails:
            csv_writer.writerow([email])

    return csv_path