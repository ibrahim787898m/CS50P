import sys

# validating command line argument
if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    # opening file and reading its lines
    with open(sys.argv[1]) as file:
        lines = file.readlines()

    # lopping through each line of file and counting each line
    count = 0
    for line in lines:

        # stripping the spaces and the new lines
        line = line.strip()

        # ignoring the comment line and the new line
        if not line or line.startswith("#"):
            continue

        count += 1

    print(count)

# checking if the file name matches
except FileNotFoundError:
    sys.exit("File does not exist")
