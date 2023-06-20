from datetime import datetime

def convert_date_format(date_string):
    original_date = datetime.strptime(date_string,'%d-%m-%Y')
    converted_date = original_date.strftime('%Y-%m-%d')
    return converted_date