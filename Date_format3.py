import re
from datetime import datetime

def recognize_date_format(date_input):
    # Convert non-string inputs to string
    if not isinstance(date_input, str):
        date_input = str(date_input)

    # Define regex patterns with their corresponding formats
    formats = [
        (r'^\d{1,2}/\d{1,2}/\d{2,4}$', ['%m/%d/%Y', '%m/%d/%y']),  # MM/DD/YYYY or MM/DD/YY
        (r'^\d{1,2}-\d{1,2}-\d{2,4}$', ['%m-%d-%Y', '%m-%d-%y']),  # MM-DD-YYYY or MM-DD-YY
        (r'^\d{1,2}-\d{1,2}-\d{2,4}$', ['%d-%m-%Y', '%d-%m-%y']),  # DD-MM-YYYY or DD-MM-YY
        (r'^\d{1,2}/\d{1,2}/\d{2,4}$', ['%d/%m/%Y', '%d/%m/%y']),  # DD/MM/YYYY or DD/MM/YY
        (r'^\d{1,2}\.\d{1,2}\.\d{2,4}$', ['%d.%m.%Y', '%d.%m.%y']),  # DD.MM.YYYY or DD.MM.YY
        (r'^\d{4}/\d{1,2}/\d{1,2}$', ['%Y/%m/%d']),  # YYYY/MM/DD
        (r'^\d{4}-\d{1,2}-\d{1,2}$', ['%Y-%m-%d']),  # YYYY-MM-DD
        (r'^\d{8}$', ['%Y%m%d']),  # YYYYMMDD
        (r'^[A-Za-z]{3}, \d{1,2} [A-Za-z]{3} \d{4}$', ['%a, %d %b %Y']),  # Day of Week, Day Month Year
        (r'^[A-Za-z]+ \d{1,2}, \d{4}$', ['%B %d, %Y']),  # Month Day, Year
        (r'^\d{1,2} [A-Za-z]+ \d{4}$', ['%d %B %Y']),  # Day Month Year
        (r'^[A-Za-z]{3} \d{1,2}, \d{4}$', ['%b %d, %Y']),  # Abbreviated Month
        (r'^\d{1,2}-\d{1,2}-\d{2}$', ['%d-%m-%y'])  # Shortened version
    ]

    # Flatten the patterns into a list of tuples for regex and formats
    checks = [(re.compile(pattern), fmt) for pattern, fmts in formats for fmt in fmts]

    # Check each combined regex and format
    for pattern, date_format in checks:
        if pattern.match(date_input):
            try:
                # Attempt to parse the date
                parsed_date = datetime.strptime(date_input, date_format)
                print(f"Recognized format: {date_format}")
                return date_format
            except ValueError:
                continue  # Invalid date, try the next format

    print("Date format not recognized.")
    return None

date_string = input("Enter the date to check the format: ")
recognize_date_format(date_string)
# Compiling the regex patterns once using re.compile() can improve performance if the function is
# called multiple times. Single Loop: It uses a single loop to check against each compiled regex and
# format, reducing the potential for quadratic time complexity. => 0(m/c.n) m=no of date formats, n=length of input date string