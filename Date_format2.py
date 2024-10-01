import re
from datetime import datetime

def recognize_date_format(date_input):
    # Convert non-string inputs to string
    if not isinstance(date_input, str):
        date_input = str(date_input)

    # Define regex patterns and corresponding formats
    # A list of tuples is used to overcome the drawback of not recognising two patterns due to overwrite
    # issue in dictionary but leveragres quadratic time complexity.
    patterns = [
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

    # Check each format
    for pattern, date_formats in patterns:
        if re.match(pattern, date_input):
            for date_format in date_formats:
                try:
                    # Attempt to parse the date to validate
                    parsed_date = datetime.strptime(date_input, date_format)
                    print(f"Recognized format: {date_format}")
                    return date_format
                except ValueError:
                    continue  # Invalid date, try the next format

    print("Date format not recognized.")
    return None

date_string = input("Enter the date to check the format: ")
recognize_date_format(date_string)
