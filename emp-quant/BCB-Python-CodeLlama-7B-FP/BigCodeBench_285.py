import mechanize
from bs4 import BeautifulSoup
def task_func(url, form_id, data):
    br = mechanize.Browser()
    br.open(url)
    br.select_form(nr=form_id)
    for key, value in data.items():
        br[key] = value
    response = br.submit()
    soup = BeautifulSoup(response, 'html.parser')
    title = soup.title.string
    if title:
        return title
    else:
        return 'No Title'
url = 'https://www.example.com/form'
form_id = 'my_form'
data = {'name': 'John Doe', 'email': 'johndoe@example.com'}