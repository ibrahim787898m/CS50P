import sys
import csv
from tabulate import tabulate

# validating command line argument
if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 2 and not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as csvfile:
        # reading all data of csv using reader function
        reader = csv.reader(csvfile)
        # storing the data from the csv as a list
        data = list(reader)
except FileNotFoundError:
    sys.exit("File does not exist")

# printing data in a table formating with header and grid
print(tabulate(data, headers="firstrow", tablefmt="grid"))
