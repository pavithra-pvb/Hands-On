import csv


#csvfile = csv.writer(open("logger.csv", "w"))
csvfile = "logger.csv"
with open(csvfile, mode = 'w') as file:
    writer = csv.writer(csvfile)
    person = {
        "first_name": "Mary",
        "last_name":  "Brown",
        "id": 2574
        }
    writer.writerow(person)
#writer = csv.writer(csvfile)
