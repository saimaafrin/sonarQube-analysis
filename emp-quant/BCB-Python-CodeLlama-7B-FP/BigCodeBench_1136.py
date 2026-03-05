import bs4
import requests
import re
import csv
def task_func(url="http://example.com", csv_path="emails.csv", 
          regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", 
          headers={'User-Agent': 'Mozilla/5.0'}):
    """
    Scrapes a web page to extract all email addresses using a specified regular expression pattern and writes them to a CSV file.
    The csv file is always created even though no email is found in the url.
    The header of the csv should be "Emails".
    """
    # Send a request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content using BeautifulSoup
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    # Find all email addresses on the page using the regular expression
    emails = re.findall(regex, soup.text)

    # Create a CSV file with the header "Emails"
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Emails'])

        # Write the extracted email addresses to the CSV file
        for email in emails:
            writer.writerow([email])

    return csv_path
url = "http://example.com"
csv_path = "emails.csv"
regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
headers = {'User-Agent': 'Mozilla/5.0'}