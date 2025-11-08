import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    """
    Counts how many times 'um' appears as a separate word in the string s,
    ignoring case and allowing for punctuation immediately after 'um'.
    """
    # \b = word boundary
    # [.,!?]? = optional punctuation immediately after 'um'
    return len(re.findall(r"\bum\b[.,!?]?", s, re.IGNORECASE))

if __name__ == "__main__":
    main()
