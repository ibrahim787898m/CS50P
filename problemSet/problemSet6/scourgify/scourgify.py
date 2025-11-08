import sys
import csv

# validating command line argument
if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

# storing fistname lastname house in seperate list
first = []
last = []
house = []

# making list of dict of all data
data = []

try:
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # spliting name into lastname and first name
            last_name, first_name = row["name"].split(", ")
            # appending to the empty list
            first.append(first_name)
            last.append(last_name)
            house.append(row["house"])
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

# appending all list items to data
for f, l, h in zip(first, last, house):
    data.append({"first" : f, "last" : l, "house" : h})

with open(sys.argv[2], "w") as csvfile:
    fieldnames = ['first', 'last', 'house']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    writer.writerows(data)

