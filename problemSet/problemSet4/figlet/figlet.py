from pyfiglet import Figlet
import sys

figlet = Figlet()

fonts = figlet.getFonts()


if len(sys.argv) == 1:
    user_input = input("Input: ")
    print(figlet.renderText(user_input))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] not in fonts:
        sys.exit("Invalid font")
    figlet.setFont(font=sys.argv[2])
    user_input = input("Input: ")
    print(figlet.renderText(user_input))
else:
    sys.exit("Invalid usage")
