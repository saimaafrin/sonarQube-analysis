
import mechanize
from bs4 import BeautifulSoup

def task_func(url, form_id, data):
    br = mechanize.Browser()
    br.open(url)
    br.select_form(id=form_id)
    for key, value in data.items():
        br[key] = value
    response = br.submit()
    soup = BeautifulSoup(response, 'html.parser')
    title = soup.title.string
    if title:
        return title
    else:
        return 'No Title'