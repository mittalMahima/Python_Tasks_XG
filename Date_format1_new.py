from datetime import datetime

# A simple list of date formats
DATE_FORMATS = [
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
]

# Corresponding names for formats for display
FORMAT_NAMES = [
    "dd/mm/yyyy",
    "dd mm yyyy",
    "dd-mm-yyyy",
    "dd.mm.yyyy",
    "ddmmyyyy",
    "yyyy-mm-dd",
    "yyyy mm dd",
    "yyyy/mm/dd",
    "yyyy.mm.dd",
    "yyyymmdd",
    "Mon dd, yyyy",
    "dd Mon yyyy",
    "dd Month yyyy",
    "ddMonyyyy",
    "ddMonthyyyy",
    "ddMon",
    "ddMonth",
    "dd Mon",
    "dd Month",
]

def identify_date_format(date_input):
    """
    Identify and return the date format for an input date.
    If it doesn't recognize or if the date is invalid, return the input date back.
    """
    # Iterate through each format in the list
    for i, format_string in enumerate(DATE_FORMATS):
        try:
            # Attempt to parse the date
            parsed_date = datetime.strptime(date_input.strip(), format_string)
            return f"Matched format: {FORMAT_NAMES[i]}"  # Return the matched format name
        except ValueError:
            continue  # If parsing fails, move to the next format

    # If no format matched, return the unrecognized message
    return f"Unrecognized or invalid date: {date_input}"

# Example usage
if __name__ == "__main__":
    while True:
        input_date = input("Enter a date (or type 'exit' to quit): ")  # Assign input_date correctly
        if input_date.lower() == 'exit':
            break
        print(identify_date_format(input_date))

# Sample input and ouput.
# Enter a date (or type 'exit' to quit): 12 july
# Matched format: dd Month
# Enter a date (or type 'exit' to quit): 12jan
# Matched format: ddMon
# Enter a date (or type 'exit' to quit): 12 jan
# Matched format: dd Mon
# Enter a date (or type 'exit' to quit): 12 jan 3456
# Matched format: dd Mon yyyy
# Enter a date (or type 'exit' to quit): 12 july 2435
# Matched format: dd Month yyyy
# Enter a date (or type 'exit' to quit): 12/10/1999
# Matched format: dd/mm/yyyy