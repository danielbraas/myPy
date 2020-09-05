# This script has been taken from: https://towardsdatascience.com/json-explained-for-python-users-data-science-edition-18e9859944da

import requests

req = requests.get("https://jsonplaceholder.typicode.com/users")
req

users = req.json()
user = users[0]

import json
# write some data into json format
with open('json_write_test.json', 'w') as f:
    json.dump(users, f, indent=4)

# Open a json file
with open('json_write_test.json') as f:
    data = json.load(f)    

for row in users:
    print(f"Address of '{row['name']} is {row['address']['street']} {row['address']['suite']}, {row['address']['city']}")

user['address']['street'], user['name']
user['address']['street']+ user['name']
