import json

#Writing to a json file
data = {
    "name": "Aarati",
    "age": 23,
    "city": "Pokhara"
}

# Writing to a JSON file
with open('example.json', 'w') as file:
    json.dump(data, file)

print("JSON file written successfully.")


#Reading from a json file
with open('example.json', 'r') as file:
    read_data = json.load(file)

print("Data read from JSON file:")
print(read_data)