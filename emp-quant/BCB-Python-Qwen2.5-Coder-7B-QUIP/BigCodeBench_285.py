
import mechanize
from bs4 import BeautifulSoup

def task_func(url, form_id, data):
    # Create a new browser instance
    br = mechanize.Browser()
    
    # Open the given URL
    br.open(url)
    
    # Select the form by its ID
    br.select_form(form_id)
    
    # Submit the form with the provided data
    br.submit(data)
    
    # Get the response content
    response = br.get_current_url()
    
    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(response, 'html.parser')
    
    # Extract the title of the page
    title = soup.title.string if soup.title else 'No Title'
    
    # Return the title as a string
    return str(title)