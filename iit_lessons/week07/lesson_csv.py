# ======================================= #
# import csv

# with open("student database.csv") as sd:
#     data = csv.reader(sd)

#     for row in data:
#         print(row[1])

# ======================================= #

# import csv

# with open("student database.csv") as sd:
#     data = csv.reader(sd)
#     next(data)

#     for row in data:
#         print(row)

# ======================================= #

# import csv

# with open("student database.csv") as sd:
#     data = csv.DictReader(sd)

#     for row in data:
#         print(row)

# ======================================= #

# import csv

# with open("student database.csv") as sd:
#     data = csv.DictReader(sd)

#     for row in data:
#         print(row["Name"])

# ======================================= #

# import csv

# with open("fruit stock.csv", "w", newline="") as fs:
#     writer = csv.writer(fs)

#     writer.writerow(["Fruit","Colour","Stock"])
#     writer.writerow(["Apple","Green",50])

# ======================================= #

import csv

with open("fruit stock.csv", "w", newline="") as fs:
    field_names = ["Fruit", "Colour", "Stock"]

    writer = csv.DictWriter(
        fs,
        fieldnames=field_names
    )

    writer.writeheader()

    writer.writerow({
        "Fruit": "Apple",
        "Colour": "Red",
        "Stock": 100
    })