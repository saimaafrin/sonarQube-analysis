import mechanize
from bs4 import BeautifulSoup
def task_func(url, form_id, data):
    # Create a browser object
    br = mechanize.Browser()
    
    # Open the URL
    br.open(url)
    
    # Select the form by its ID
    br.select_form(nr=form_id)
    
    # Submit the form with the provided data
    response = br.submit(None, data)
    
    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(response.get_data(), 'html.parser')
    
    # Extract the title of the page
    title = soup.title.string if soup.title else 'No Title'
    
    return title