def convert(text):
    # Replace :) with 🙂 and :( with 🙁
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_input = input()
    print(convert(user_input))

# Ensure main runs when the script is executed directly
if __name__ == "__main__":
    main()
