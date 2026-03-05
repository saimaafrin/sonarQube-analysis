import mechanize
from bs4 import BeautifulSoup
def task_func(url, form_id, data):
    # Create a browser instance
    br = mechanize.Browser()
    
    # Open the URL
    br.open(url)
    
    # Select the form by its ID
    br.select_form(nr=form_id)
    
    # Submit the form with the provided data
    br.submit(form=br.form, data=data)
    
    # Get the response page
    response = br.response()
    
    # Parse the response page with BeautifulSoup
    soup = BeautifulSoup(response.read(), 'html.parser')
    
    # Extract the title of the page
    title = soup.title.string if soup.title else 'No Title'
    
    # Return the title
    return title