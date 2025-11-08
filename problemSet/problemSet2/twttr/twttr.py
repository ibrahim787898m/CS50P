def main():
    userInput = input("Input: ")
    print("Output:", twttr(userInput))

def twttr(name):
        return name.translate(str.maketrans("", "", "aeiouAEIOU"))

if __name__ == "__main__":
    main()
