def main():
    get_items()

def get_items():
    # creating empty dict
    groceries = {}

    while True:
        try:
            item = input().lower()

            # using hash map to store the items and it's count
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1

        except EOFError:
            break

    # using loop to sort alphabetically
    for item in sorted(groceries.keys()):
        print(groceries[item], item.upper())

if __name__ == "__main__":
    main()

