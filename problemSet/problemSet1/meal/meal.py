def main():
    userInput = input("What time is it? ")
    t = convert(userInput)

    if 8 >= t >= 7:
        print("breakfast time")
    elif 13 >= t >= 12:
        print("lunch time")
    elif 21 >= t >= 18:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    time = hours + minutes / 60
    return time


if __name__ == "__main__":
    main()
