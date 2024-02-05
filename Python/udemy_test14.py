import csv


#csvfile = csv.writer(open("logger.csv", "w"))
csvfile = "logger.csv"
with open(csvfile, 'w', newline="") as file:
    writer = csv.writer(csvfile)
    person = {
        "first_name": "Mary",
        "last_name":  "Brown",
        "id": 2574
    }
    fields = ['first_name', 'last_name', 'id']
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writerow(person)