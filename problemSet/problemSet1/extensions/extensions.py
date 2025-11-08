def main():
    userInput = input("File name: ")
    userInput = userInput.strip().lower()
    output(userInput)

def output(uIn):
    if uIn.endswith(".gif"):
        print("image/gif")
    elif uIn.endswith(".jpg") or uIn.endswith(".jpeg"):
        print("image/jpeg")
    elif uIn.endswith(".png"):
        print("image/png")
    elif uIn.endswith(".pdf"):
        print("application/pdf")
    elif uIn.endswith(".txt"):
        print("text/plain")
    elif uIn.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()
