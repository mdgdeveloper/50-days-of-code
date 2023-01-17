# Write a function called save_json. This function takes a
# dictionary below as an argument and saves it on a file in JSON
# format.
# Write another function called read_json that opens the file
# that you just saved and reads its content.

import json


def save_json(info):
    jsondata = json.dumps(info)
    with open('json_data.json', 'w') as outfile:
        outfile.write(jsondata)


def read_json():
    with open('json_data.json', 'r') as readfile:
        jsondata = json.load(readfile)
        print(jsondata)


# Test
names = {'name': 'Carol', 'sex': 'female', 'age': 55}
save_json(names)
read_json()
