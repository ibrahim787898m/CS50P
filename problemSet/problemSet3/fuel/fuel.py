def main():
    numerator, denominator = get_fraction()

    percent = round((numerator / denominator) * 100)

    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")




def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            numerator, denominator = fraction.split("/")
            numerator = int(numerator)
            denominator = int(denominator)

            if numerator > denominator or numerator < 0 or denominator < 0:
                continue

            return numerator, denominator

        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
















# def main():
#     numerator, denominator = get_fraction()
#     percent = round((numerator / denominator) * 100)

#     if percent <= 1:
#         print("E")
#     elif percent >= 99:
#         print("F")
#     else:
#         print(f"{percent}%")

# def get_fraction():
#     while True:
#         fraction = input("Fraction: ").strip()
#         if "/" not in fraction:
#             continue

#         store = fraction.split("/")

#         # Must have exactly 2 parts
#         if len(store) != 2:
#             continue

#         # Check if both are integers
#         if not store[0].isdigit() or not store[1].isdigit():
#             continue

#         numerator = int(store[0])
#         denominator = int(store[1])

#         # Denominator cannot be 0
#         if denominator == 0:
#             continue

#         # Numerator cannot be bigger than denominator
#         if numerator > denominator:
#             continue

#         return (numerator, denominator)


# if __name__ == "__main__":
#     main()





# fraction = input("Fraction: ")

# store = fraction.split("/")

# percent = (int(store[0]) / int(store[1])) * 100

# percent = int(percent)

# print(percent,"%", sep="")
