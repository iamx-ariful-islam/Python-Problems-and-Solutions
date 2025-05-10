from datetime import datetime


# get the weekday name based on date
def get_weekday(date_string, format='%d.%m.%Y'):
    date_obj = datetime.strptime(date_string, format)
    return date_obj.strftime(f'{date_string} = %A')
    

print(get_weekday('11.02.2024'))


'''output:

11.02.2024 = Sunday
'''
