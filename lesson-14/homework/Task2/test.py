import requests
from bs4 import BeautifulSoup

# URL of the job posting
url = "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"

# Send a GET request to fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find('h1', class_  = "title is-2")
# Extracting location and date
location = soup.find('p', id='location').text if soup.find('p', id='location') else "Location not found"
date = soup.find('p', id='date').text if soup.find('p', id='date') else "Date not found"
print(title.text)
print(f"Location: {location}")
print(f"Date: {date}")
