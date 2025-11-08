import random

def main():
    level = get_level()
    count = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        for _ in range(3):
            try:
                user_input = int(input(f"{x} + {y} = "))
                if user_input == answer:
                    count += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {answer}")

    print("Score:", count)

def get_level():
    while True:
        try:
            n = input("Level: ")
            n = int(n)
            if n != 1 and n != 2 and n != 3:
                continue
            return n

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
