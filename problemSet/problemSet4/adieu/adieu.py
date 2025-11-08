import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        names += [name]
    except EOFError:
        break

print()
print(f"Adieu, adieu, to {p.join(names)}")

# output = p.join(("apple", "banana", "carrot"))

# print(output)
