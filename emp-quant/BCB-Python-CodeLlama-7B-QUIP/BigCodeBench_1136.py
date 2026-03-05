
import bs4
import requests
import re
import csv

def task_func(url="http://example.com", csv_path="emails.csv", 
          regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", 
          headers={'User-Agent': 'Mozilla/5.0'}):
    # Create a CSV file to store the extracted email addresses
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Emails"])

    # Send a request to the web page
    response = requests.get(url, headers=headers)

    # Parse the HTML content of the web page
    soup = bs4.BeautifulSoup(response.content, "html.parser")

    # Find all the email addresses in the web page using the regular expression
    email_addresses = re.findall(regex, soup.text)

    # Write the email addresses to the CSV file
    for email in email_addresses:
        csv_writer.writerow([email])

    # Return the path to the CSV file
    return csv_path