# import Libraries
import json
import csv

# Opening the file & Storing
with open ('JSON File Example.jsonl') as json_file:
    data = json.load(json_file)

data_file = open('data_file.csv','w', newline='')
csv_writer = csv.writer(data_file)
print(data['ROV Depth'])

# Rewriting the file
count = 0
seconds = "Seconds"
depth = "Depth"
csv_writer.writerow([seconds, depth])
for entry in data['ROV Depth']:
    seconds = entry["Seconds"]
    depth = entry["Height"]
    csv_writer.writerow([seconds, depth])

data_file.close()

# This is what would be printed out in the CSV FIle you can put this into Google or Excel
# Seconds,Depth
1,"['5 ft', '9 in']"
2,"['5 ft', '10 in']"
3,"['6 ft', '0 in']"
4,"['6 ft', '5 in']"
5,"['6 ft', '9 in']"
6,"['7 ft', '3 in']"
7,"['7 ft', '8 in']"
8,"['8 ft', '3 in']"
9,"['9 ft', '4 in']"
10,"['9 ft', '10 in']"
11,"['10 ft', '0 in']"
12,"['10 ft', '9 in']"


