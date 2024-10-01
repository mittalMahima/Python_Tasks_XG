from datetime import datetime

def recognize_date_format(date_input):
    # Convert non-string inputs to string
    if not isinstance(date_input, str):
        date_input = str(date_input)

    # Define possible date formats in a list
    formats = [
        '%m/%d/%Y', '%m/%d/%y',  # MM/DD/YYYY or MM/DD/YY
        '%d-%m-%Y', '%d-%m-%y',  # DD-MM-YYYY or DD-MM-YY
        '%m-%d-%Y', '%m-%d-%y',  # MM-DD-YYYY or MM-DD-YY
        '%d/%m/%Y', '%d/%m/%y',  # DD/MM/YYYY or DD/MM/YY
        '%d.%m.%Y', '%d.%m.%y',  # DD.MM.YYYY or DD.MM.YY
        '%Y/%m/%d',              # YYYY/MM/DD
        '%Y-%m-%d',              # YYYY-MM-DD
        '%Y%m%d',                # YYYYMMDD
        '%a, %d %b %Y',         # Day of Week, Day Month Year  # Eg. "Fri, 30 Mar 2022" not "Friday, 30 Mar 2022" without "" as Fri can't be converted to int.
        '%B %d, %Y',            # Month Day, Year
        '%d %B %Y',              # Day Month Year
        '%b %d, %Y',            # Abbreviated Month
        '%d-%m-%y'               # Shortened version
    ]

    # Check each format in the list
    for date_format in formats:
        try:
            # Attempt to parse the date
            parsed_date = datetime.strptime(date_input, date_format)
            print(f"Recognized format: {date_format}")
            return date_format
        except ValueError:
            continue  # Invalid date format, try the next one

    print("Date format not recognized.")
    return None

date_string = input("Enter the date to check the format: ")
recognize_date_format(date_string)
