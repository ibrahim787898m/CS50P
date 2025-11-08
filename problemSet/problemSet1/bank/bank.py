def main():
    userInput = input("Gretting: ")
    userInput = userInput.strip().lower()
    output(userInput)

def output(uIn):
    if uIn.startswith("hello"):
        print("$0")
    elif uIn.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
