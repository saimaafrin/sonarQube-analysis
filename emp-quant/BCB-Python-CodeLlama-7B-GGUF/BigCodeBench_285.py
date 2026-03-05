
import mechanize
from bs4 import BeautifulSoup

def task_func(url, form_id, data):
    br = mechanize.Browser()
    br.open(url)
    form = br.select_form(id=form_id)
    for key, value in data.items():
        form[key].value = value
    br.submit()
    response = br.response()
    soup = BeautifulSoup(response, 'html.parser')
    title = soup.title.string
    if title:
        return title
    else:
        return 'No Title'