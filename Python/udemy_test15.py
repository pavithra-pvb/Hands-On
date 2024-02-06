import csv


csvfile = csv.writer(open("logger.csv", "w"))

#with open(csvfile, mode = 'w') as file:
person = {
        "first_name": "Mary",
        "last_name":  "Brown",
        "id": 2574
        }

writer = csv.DictWriter(csvfile)
writer.writerow(person)