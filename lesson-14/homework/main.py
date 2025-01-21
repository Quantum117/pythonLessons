from bs4 import BeautifulSoup
from pathlib import Path
html_doc = 'weather.html'
with open(html_doc, 'r') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

print(soup.title)