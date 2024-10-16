from datetime import datetime

def identify_date_format(date_input):
    """
    Identify and return the date format for an input date.
    If it doesn't recognize or if the date is invalid, return the input date back.
    """
    # Define possible date formats in a simple list
    formats = [
        '%d/%m/%Y',  # dd/mm/yyyy
        '%d %m %Y',  # dd mm yyyy
        '%d-%m-%Y',  # dd-mm-yyyy
        '%d.%m.%Y',  # dd.mm.yyyy
        '%d%m%Y',    # ddmmyyyy
        '%Y-%m-%d',  # yyyy-mm-dd
        '%Y %m %d',  # yyyy mm dd
        '%Y/%m/%d',  # yyyy/mm/dd
        '%Y.%m.%d',  # yyyy.mm.dd
        '%Y%m%d',    # yyyymmdd
        '%b %d, %Y', # Mon dd, yyyy
        '%d %b %Y',  # dd Mon yyyy
        '%d %B %Y',  # dd Month yyyy
        '%d%b%Y',    # ddMonyyyy
        '%d%B%Y',    # ddMonthyyyy
        '%d%b',      # ddMon
        '%d%B',      # ddMonth
        '%d %b',     # dd Mon
        '%d %B',     # dd Month
        '%d%Y',      # ddMMyyyy
        '%d %B',     # Allow both "12 July" and "12July"
        '%d%b',      # e.g. "12Jul"
        '%d %b',     # e.g. "12 Jul"
    ]

    for date_format in formats:
        try:
            # Attempt to parse the date
            parsed_date = datetime.strptime(date_input.strip(), date_format)
            return f"Matched date format is: {date_format}"  # Return the matched format
        except ValueError:
            continue  # Invalid date format, try the next one

    return f"Unrecognized or invalid date input: {date_input}"

if __name__ == "__main__":
    while True:
        date_string = input("Enter the date to check the format (or type 'exit' to quit): ")
        if date_string.lower() == 'exit':
            break
        print(identify_date_format(date_string))


#Sample input and output.
# Enter the date to check the format (or type 'exit' to quit): 1jan
# Matched date format is: %d%b
# Enter the date to check the format (or type 'exit' to quit): 1 Jan
# Matched date format is: %d %b
# Enter the date to check the format (or type 'exit' to quit): 12 july 4567
# Matched date format is: %d %B %Y
# Enter the date to check the format (or type 'exit' to quit): 12 jan 4567
# Matched date format is: %d %b %Y
# Enter the date to check the format (or type 'exit' to quit): 12jan3567
# Matched date format is: %d%b%Y
# Enter the date to check the format (or type 'exit' to quit): 12July3456
# Matched date format is: %d%B%Y
