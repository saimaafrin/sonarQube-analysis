
import mechanize
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def task_func(url):
    browser = mechanize.Browser()
    page = browser.open(url)
    soup = BeautifulSoup(page, "html.parser")
    links = soup.find_all("a")
    for link in links:
        if link.get("href"):
            link_url = urljoin(url, link.get("href"))
            print(link_url)
    return links