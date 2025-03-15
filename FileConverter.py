# import Libraries
import json
import csv

# Opening the file & Storing
with open ('JSON File Example.jsonl') as json_file:
    data = json.load(json_file)

data_file = open('data_file.csv','w', newline='')
csv_writer = csv.writer(data_file)

# Rewriting the file
count = 0
for entry in data:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())

data_file.close()

# The file is rewritten as a CSV file given the data is like this
# ('Age': 18, 'Name': 'Jeremy Cortez', 'Height': 5 9, 'Gender': 'Male')


