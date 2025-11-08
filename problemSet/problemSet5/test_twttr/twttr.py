def main():
    userInput = input("Input: ")
    print("Output:", shorten(userInput))

def shorten(name):
    return name.translate(str.maketrans("", "", "aeiouAEIOU"))

if __name__ ==  "__main__":
    main()
