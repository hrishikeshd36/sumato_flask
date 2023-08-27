import json

# Open the JSON file and load its contents into a dictionary
with open('data.json') as json_file:
    my_data = json.load(json_file)

# Print the dictionary and its type
print(my_data)
print(type(my_data))


