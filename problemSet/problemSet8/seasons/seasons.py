from datetime import datetime, date
import inflect
import sys

def main():
    bdate_str = input("Date of Birth: ")

    try:
        # changing date string to date object
        b_date = datetime.strptime(bdate_str, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date")

    minutes = calculate_minutes(b_date)

    p = inflect.engine()

    # converting minutes from number form to word form
    mins_words = p.number_to_words(minutes, andword="").capitalize()

    print(f"{mins_words} minutes")



def calculate_minutes(birthdate: date) -> int:
    # getting todays date
    today = date.today()
    # getting days between these 2 date
    diff = today - birthdate

    # converting days into minutes and returning as an integer
    return diff.days * 24 * 60


if __name__ == "__main__":
    main()
