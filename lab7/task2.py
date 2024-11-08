import json


with open("ex_2_formatted.json") as file:
    data = json.load(file)
    phones = {}
    
    for user in data["users"]:
        phones[user["name"]] = user["phoneNumber"]

    print(phones)