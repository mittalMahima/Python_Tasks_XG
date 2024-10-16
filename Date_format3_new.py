import re
from datetime import datetime

# A list of common date patterns with corresponding formats
DATE_PATTERNS = [
    (r'\b(\d{1,2}/\d{1,2}/\d{4})\b', "dd/mm/yyyy"),   # 12/10/2024
    (r'\b(\d{1,2} \d{1,2} \d{4})\b', "dd mm yyyy"),   # 12 10 2024
    (r'\b(\d{1,2}-\d{1,2}-\d{4})\b', "dd-mm-yyyy"),   # 12-10-2024
    (r'\b(\d{1,2}\.\d{1,2}\.\d{4})\b', "dd.mm.yyyy"), # 12.10.2024
    (r'\b(\d{1,2}\d{1,2}\d{4})\b', "ddmmyyyy"),       # 12102024
    (r'\b(\d{4}-\d{1,2}-\d{1,2})\b', "yyyy-mm-dd"),   # 2024-10-12
    (r'\b(\d{4}/\d{1,2}/\d{1,2})\b', "yyyy/mm/dd"),   # 2024/10/12
    (r'\b(\d{4}\.\d{1,2}\.\d{1,2})\b', "yyyy.mm.dd"),  # 2024.10.12
    (r'\b(\d{4} \d{1,2} \d{1,2})\b', "yyyy mm dd"),    # 2024 10 12
    (r'\b(\d{4}\d{1,2}\d{1,2})\b', "yyyymmdd"),        # 20241012
    (r'\b([A-Za-z]{3}\s+\d{1,2},?\s+\d{4})\b', "Mon dd, yyyy"),  # Oct 12, 2024
    (r'\b(\d{1,2}\s+[A-Za-z]{3}\s+\d{4})\b', "dd Mon yyyy"),  # 12 Oct 2024
    (r'\b(\d{1,2}\s+[A-Za-z]{4,9}\s+\d{4})\b', "dd Month yyyy"),  # 12 October 2024
    (r'\b(\d{1,2}[A-Za-z]{3}\d{4})\b', "ddMonyyyy"),  # 12Oct2024
    (r'\b(\d{1,2}[A-Za-z]{4,9}\d{4})\b', "ddMonthyyyy"),  # 12October2024
    (r'\b(\d{1,2}[A-Za-z]{3})\b', "ddMon"),  # 12Oct
    (r'\b(\d{1,2}[A-Za-z]{4,9})\b', "ddMonth"),  # 12October
    (r'\b(\d{1,2}\s+[A-Za-z]{3})\b', "dd Mon"),  # 12 Oct
    (r'\b(\d{1,2}\s+[A-Za-z]{4,9})\b', "dd Month"),  # 12 October
]

def identify_date_format(date_input):
    """
    Identify and return the date format for an input date.
    If it doesn't recognize or if the date is invalid, return the input date back.
    """
    # Match input with regular expressions to identify format
    for pattern, date_format in DATE_PATTERNS:
        match = re.fullmatch(pattern, date_input)  # Use fullmatch to ensure complete match
        if match:
            # Check if the date is valid using datetime
            try:
                # Parse the date according to the matched pattern
                if date_format == "dd/mm/yyyy":
                    day, month, year = map(int, date_input.split('/'))
                    datetime(year, month, day)
                elif date_format == "dd mm yyyy":
                    day, month, year = map(int, date_input.split())
                    datetime(year, month, day)
                elif date_format == "dd-mm-yyyy":
                    day, month, year = map(int, date_input.split('-'))
                    datetime(year, month, day)
                elif date_format == "dd.mm.yyyy":
                    day, month, year = map(int, date_input.split('.'))
                    datetime(year, month, day)
                elif date_format == "yyyy-mm-dd":
                    year, month, day = map(int, date_input.split('-'))
                    datetime(year, month, day)
                elif date_format == "yyyy/mm/dd":
                    year, month, day = map(int, date_input.split('/'))
                    datetime(year, month, day)
                elif date_format == "yyyy.mm.dd":
                    year, month, day = map(int, date_input.split('.'))
                    datetime(year, month, day)
                elif date_format == "yyyy mm dd":
                    year, month, day = map(int, date_input.split())
                    datetime(year, month, day)
                elif date_format == "Mon dd, yyyy":
                    datetime.strptime(date_input, "%b %d, %Y")
                elif date_format == "dd Mon yyyy":
                    day, month, year = re.split(r'\s+', date_input)
                    datetime.strptime(f"{day} {month} {year}", "%d %b %Y")
                elif date_format == "dd Month yyyy":
                    day, month, year = re.split(r'\s+', date_input)
                    datetime.strptime(f"{day} {month} {year}", "%d %B %Y")
                elif date_format == "ddMonyyyy":
                    day = int(date_input[:-7])
                    month = datetime.strptime(date_input[-7:-4], "%b").month
                    year = int(date_input[-4:])
                    datetime(year, month, day)
                elif date_format == "ddMonthyyyy":
                    day = int(date_input[:-8])
                    month = datetime.strptime(date_input[-8:-4], "%B").month
                    year = int(date_input[-4:])
                    datetime(year, month, day)
                elif date_format == "ddMon":
                    day = int(date_input[:-3])
                    month = datetime.strptime(date_input[-3:], "%b").month
                    datetime(2000, month, day)  # Using a placeholder year
                elif date_format == "dd Mon":
                    day, month = re.split(r'\s+', date_input)
                    datetime(2000, datetime.strptime(month, "%b").month, int(day))  # Using a placeholder year
                # If parsing succeeded, return the matched format
                return f"Matched format: {date_format}"
            except ValueError:
                # If parsing failed, return the unrecognized message
                return f"invalid date: {date_input}"

    # If no regex pattern matched, return the input as unrecognized
    return f"Unrecognized or invalid date: {date_input}"

# Example usage
if __name__ == "__main__":
    while True:
        input_date = input("Enter a date (or type 'exit' to quit): ")
        if input_date.lower() == 'exit':
            break
        print(identify_date_format(input_date))

# Enter a date (or type 'exit' to quit): 31/02/1027    sample input output.
# invalid date: 31/02/1027
# Enter a date (or type 'exit' to quit): 31/04/1090
# invalid date: 31/04/1090
# Enter a date (or type 'exit' to quit):