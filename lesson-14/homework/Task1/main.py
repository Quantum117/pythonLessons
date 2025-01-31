from bs4 import BeautifulSoup
import numpy as np
import pprint

html_doc = 'weather.html'
with open(html_doc, 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

class Weather :
    def __init__(self, day, temperature, condition):
        self.day = day
        self.temperature = temperature
        self.day = day
        
# Extract rows from the table body
table = soup.find('tbody')
rows = table.find_all('tr')

# Parse each row
forecast = []
for row in rows:
    cols = row.find_all('td')  # Find all <td> in the row
    day = cols[0].text.strip()  # Extract day
    temp = cols[1].text.strip()  # Extract temperature
    condition = cols[2].text.strip()  # Extract condition
    forecast.append({'day': day, 'temperature': temp, 'condition': condition})

pprint.pprint(forecast)

# extract single number from a line
def number_extract(line):
    number =''
    for char in line :
        if char.isdigit():
            number += char
    return int(number)

temperatures = [number_extract(item['temperature']) for item in forecast]
sunny_days = [item for item in forecast if item['condition'] == 'Sunny']
highest_temperature = [item for item in forecast if item['temperature'] == max(temperatures)]
print(temperatures)
print(f'average weekly temperature {np.array([temperatures]).mean()}')
pprint.pprint(sunny_days)
