def main():
    # calling database function in main function to use it in convert function
    months = database()
    convert(months)


# function for database of months
def database():
    return {
        "January" : "01",
        "February" : "02",
        "March" : "03",
        "April" : "04",
        "May" : "05",
        "June" : "06",
        "July" : "07",
        "August" : "08",
        "September" : "09",
        "October" : "10",
        "November" : "11",
        "December" : "12"
        }


# function for converting date format
def convert(months):

    while True:
        # getting user input for date
        date_input = input("Date: ")

        try:
            # storing date input in a list named parts
            parts = date_input.strip().split("/")

            # storing each list item in seperate variable
            str_month, str_day, str_year = parts

            # converting each stored string into integer
            int_month = int(str_month)
            int_day = int(str_day)
            int_year = int(str_year)

            # checking if month(1 - 12) and day(1 - 31)
            if 1 <= int_month <= 12 and 1 <= int_day <= 31:
                # printing date in YYYY/MM/DD format
                print(f"{int_year}-{str_month.zfill(2)}-{str_day.zfill(2)}")
                break

        except ValueError:
            pass



        try:
            # checking if date input contain "," or not in a different format
            if "," not in date_input:
                continue

            # storing date input in a list named parts
            parts = date_input.replace(",", "").split()

            # checking if the length of the parts 3 or not
            if len(parts) != 3:
                continue

            # storing each list item in seperate variable
            str_month_name, str_day, str_year = parts


            # getting keys from the months dict
            months_keys = months.keys()

            # checking if stored month name in the months keys or not
            if str_month_name not in months_keys:
                continue

            # getting the value of months according the the str month name
            str_month_num = months.get(str_month_name)

            # converting each stored string into integer
            int_month = int(str_month_num)
            int_day = int(str_day)
            int_year = int(str_year)

            # checking if month(1 - 12) and day(1 - 31)
            if 1 <= int_month <= 12 and 1 <= int_day <= 31:
                # printing date in YYYY/MM/DD format
                print(f"{int_year}-{str_month_num}-{str_day.zfill(2)}")
                break

        except ValueError:
            pass


if __name__ == "__main__":
    main()
