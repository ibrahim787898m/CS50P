import random

while True:
    try:
        # n here is level that is the range of gussing a rand num
        n = input("Level: ")
        n = int(n)
        # checking for nonpositive number
        if n <= 0:
            continue
        break
    
    except ValueError:
        pass

# storing a random number from 1 to n
rand_num = random.randint(1, int(n))

while True:
    try:
        guess = input("Guess: ")

        guess = int(guess)

        # checking for nonpositive number
        if guess <= 0:
            continue

        # checking if the guess num is matched with rand num or not
        if guess < rand_num:
            print("Too small!")
        elif guess > rand_num:
            print("Too large!")
        else:
            print("Just right!")
            break

    except ValueError:
        pass
