import csv
import json
from bs4 import BeautifulSoup
import requests

# Fetch the webpage
res = requests.get('https://books.toscrape.com/')
res.raise_for_status()  # Check if the request was successful

# Write the HTML content to a file
with open('taskdata.html', 'w') as f:
    f.write(res.text)

# Parse the HTML content using BeautifulSoup with the 'html.parser'
soup = BeautifulSoup(res.text, 'html.parser')

# Find all the book entries
books = soup.find_all('article', class_="product_pod")

# Prepare data for CSV and json
data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").get_text().strip()
    rating = book.p["class"][1]
    stock = book.find("p", class_="instock availability").get_text().strip()
    data.append([title, price, rating, stock])

    # For debugging purposes
    print('Title:', title)
    print('Price:', price)
    print('Rating:', rating)
    print('Stock:', stock)

# Writing to a CSV file
with open('taskexample.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Rating', 'Stock'])  # Write header
    writer.writerows(data)  # Write data

print("CSV file written successfully.")

# Reading from a CSV file
with open('taskexample.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing to a JSON file
with open('taskexample.json', 'w',newline='', encoding='utf-8') as file:
    json.dump(data, file, indent = 2)

print("JSON file written successfully.")


#Reading from a json file
with open('taskexample.json', 'r',newline='', encoding='utf-8') as file:
    read_data = json.load(file)

print("Data read from JSON file:")
print(read_data)