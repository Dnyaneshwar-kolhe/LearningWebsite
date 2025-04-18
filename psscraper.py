import requests
from bs4 import BeautifulSoup


with open("sample.html","r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.get_text())



#req = requests.get("project.html")

#soup = BeautifulSoup(req.content, "html.parser")