def main():
    c = 300000000;
    m = int(input("m: "))
    print("e:", calculate(m, c))

def calculate(m, c):
    e = m * (c * c)
    return e

if __name__ == "__main__":
    main()
