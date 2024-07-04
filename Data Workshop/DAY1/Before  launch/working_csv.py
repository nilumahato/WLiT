import csv

#Writing to a csv file

data = [
    ["Name", "Age", "City"],
    ["Aarati", 20, "Pokhara"],
    ["Nilu", 23, "Bayalbas"],

]

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data)

print("csv file written succesfully.")

#Reading from a csv file
with open('example.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
