
import bs4
import requests
import re
import csv

def task_func(url="http://example.com", csv_path="emails.csv", 
              regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", 
              headers={'User-Agent': 'Mozilla/5.0'}):
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content using BeautifulSoup
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    # Find all email addresses in the HTML content using the regular expression
    emails = re.findall(regex, soup.text)

    # Create a CSV file with the header "Emails"
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Emails'])

        # Write the email addresses to the CSV file
        for email in emails:
            writer.writerow([email])

    # Return the path to the CSV file
    return csv_path

# Call the function with the specified URL and CSV file path
csv_path = task_func(url="http://example.com", csv_path="emails.csv")
print(csv_path)