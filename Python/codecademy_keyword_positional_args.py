import reqs as requests
from bs4 import BeautifulSoup

def get_id(html_id, website="http://coolsite.com"):
  request = requests.get(website)
  parsed_html = BeautifulSoup(website.content, features="html.parser")
  return parsed_html.find(id_=html_id)
