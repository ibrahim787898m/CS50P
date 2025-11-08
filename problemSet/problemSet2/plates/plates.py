def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s[0:2].isalpha():
        return False

    for i, ch in enumerate(s):
        if ch.isdigit():
            if ch == "0" and i == s.find(ch):
                return False

            if not s[i:].isdigit():
                return False

            break

    if not s.isalnum():
        return False


    return True

if __name__ == "__main__":
    main()
