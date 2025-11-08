def main():
    userInput = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    userInput = userInput.strip().lower()
    output(userInput)

def output(uIn):
    if uIn == "42" or uIn == "forty two" or uIn == "forty-two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()




# userinput = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# userinput = userinput.lower().strip()

# if userinput == "42":
#     print("Yes")
# elif userinput == "forty two" or userinput == "forty-two":
#     print("Yes")
# else:
#     print("No")
