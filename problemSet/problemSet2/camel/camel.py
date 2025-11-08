def main():
    camel = input("camelCase: ")
    print("snake_case:", camel_to_snake(camel))

def camel_to_snake(name):
    snake = ""
    for ch in name:
        if ch.isupper():
            snake += "_" + ch.lower()
        else:
            snake += ch
    return snake

if __name__ == "__main__":
    main()
