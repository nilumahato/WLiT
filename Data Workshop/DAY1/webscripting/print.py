import csv
import json
import requests
from bs4 import BeautifulSoup

# Fetch the webpage
res = requests.get('https://books.toscrape.com/')

# Print the status code to ensure the request was successful
print(res.status_code)

# Print the response object
print(res)

# Print the HTML content of the page
print(res.text)

# Write the HTML content to a file
with open('data.html', 'w') as f:
    f.write(res.text)

# Parse the HTML content using BeautifulSoup with the 'html.parser'
soup = BeautifulSoup(res.text, 'html.parser')

print(soup)

# Find all the <h3> tags which contain book titles
titles = soup.find_all('h3')

# Print the number of titles found
print(f'Number of titles found: {len(titles)}')

data=[]
for t in titles:
    data.append(t.get_text())
    #print(t.get_text())

# Print the text of the title at index 2 (third title)
# print(titles[2].text)
   
# Iterate over each title and print its text using t.get_text()
# for t in titles:
#     print(t.get_text().strip())  # .strip() is used to remove any leading/trailing whitespace


# with open('tittles.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(titles)

# print("csv file written succesfully.")


# #Reading from a csv file
# with open('tittles.csv', 'r', newline='') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


#Writing to a json file
with open('data.json', 'w') as f:
    json.dump(data, f, indent = 2)


#Reading from a json file
with open('data.json', 'r') as f:
    read_data = json.load(f)

print("Data read from JSON file:")
print(read_data)