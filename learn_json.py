import json
from typing import IO
from urllib.request import urlopen
with urlopen("https://open.er-api.com/v6/latest/USD") as response:
    source = response.read()

data = json.loads(source)
# print(json.dumps(data, indent=2))
# print(type(data['rates']))
json_data = json.dumps(data['rates'])
print(type(json.loads(json_data)))
with open("data.json", "w") as file:
        file: IO[str] = file
        json.dump(data, file, indent = 4)
with open("data.json", "r") as file:
 print(type(file))