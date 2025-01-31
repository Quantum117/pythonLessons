from bs4 import  BeautifulSoup
import  requests
import sqlite3

base_Url = 'https://realpython.github.io/fake-jobs/'

# get html content from base url
html = requests.get(base_Url)
soup = BeautifulSoup(html.text, 'html.parser')
# every job is located inside a tag so we get all of them
a = soup.find_all('a')

# getting job urls from a tags in every job
urls = [item['href'] for item in a if item.text == 'Apply']

# jobs list
jobs =[]

# looping through every job url
for url in urls :
    content = requests.get(url)
    b_soup = BeautifulSoup(content.text, 'html.parser')
    title = b_soup.find('h1', class_ = "title is-2").text
    company = b_soup.find('h2', class_ = "subtitle is-4 company").text
    description = b_soup.find('div', class_ = "content").find('p').text
    location = b_soup.find('p', id = 'location').text.replace("Location: ", '')
    date = b_soup.find('p', id = 'date').text.replace("Posted: ", '')
    jobs.append({'title': title, 'description': description, 'location': location, 'date': date})

#print items from jobs
for item in jobs:
    print(item)