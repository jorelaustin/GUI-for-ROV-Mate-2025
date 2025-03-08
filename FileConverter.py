# import Libraries
import json
import csv

# Opening the file & Storing
with open ('json.file') as json_file:
    data = json.load(json_file)

data_file = open('data_file.csv','w', newline'')
csv_writer = csv.writer(data_file)

# Rewriting the file
count = 0
for data in jsondata:
    if count == 0:
        header = content1.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())

data_file.close()

# The file is rewritten as a CSV file given the data is like this
# ('Age': 18, 'Height': 5, 'Gender': 'Male')





























import csv

