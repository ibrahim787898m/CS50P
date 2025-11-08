import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regex: captures start time + AM/PM + end time + AM/PM
    match = re.fullmatch(r'(\d{1,2}(?::\d{2})?) (AM|PM) to (\d{1,2}(?::\d{2})?) (AM|PM)', s)
    if not match:
        raise ValueError("Invalid format")

    start, start_meridiem, end, end_meridiem = match.groups()

    return f"{to_24h(start, start_meridiem)} to {to_24h(end, end_meridiem)}"


def to_24h(time_str, meridiem):
    # Split hours and minutes
    if ":" in time_str:
        hour, minute = map(int, time_str.split(":"))
    else:
        hour, minute = int(time_str), 0

    # Validate values
    if hour < 1 or hour > 12 or minute < 0 or minute > 59:
        raise ValueError("Invalid time")

    # Convert to 24-hour format
    if meridiem == "AM":
        if hour == 12:  # 12 AM → 00
            hour = 0
    else:  # PM
        if hour != 12:  # 12 PM → 12, others add 12
            hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
