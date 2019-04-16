import csv

with open("Top1000Songs.csv") as file:
    reader = csv.reader(file)

    count = 0

    for row in(reader):
        print(row)

        if count > 5:
            break

        count =+ 1


