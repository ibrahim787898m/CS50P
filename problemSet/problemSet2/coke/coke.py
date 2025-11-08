def main():
    amount_due = 50
    valid_coin = [25, 10, 5]

    while True:
        print("Amount due:", amount_due)

        insert_coin = int(input("Insert coin: "))
        if insert_coin not in valid_coin:
            continue

        amount_due -= insert_coin

        if amount_due <= 0:
            break

    print("Change Owed:", abs(amount_due))

main()





# x = 50
# print("Amount due:", x)
# y = int(input("Insert coin: "))
# x -= y
# print("Amount due:", x)
