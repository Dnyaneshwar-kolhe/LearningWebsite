import requests
from bs4 import BeautifulSoup

with open("project.html","r") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
r= soup.title
print(soup.prettify())