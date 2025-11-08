userInput = input("Expression: ")
userInput = userInput.strip()

x, y, z = userInput.split()

x = int(x)
z = int(z)

if y == "+":
    ans = x + z
    ans = float(ans)
    ans = round(ans, 1)
elif y == "-":
    ans = x - z
    ans = float(ans)
    ans = round(ans, 1)
elif y == "*":
    ans = x * z
    ans = float(ans)
    ans = round(ans, 1)
elif y == "/":
    ans = x / z
    ans = float(ans)
    ans = round(ans, 1)

print(ans)
