# pip install pybengali

import pybengali


today = pybengali.today()
print(today)

today = pybengali.today(day="04", month="10", year="2022")
print(today)

tomorrow = pybengali.tomorrow()
print(tomorrow)

yesterday = pybengali.yesterday()
print(yesterday)

timesince = pybengali.timesince(day="04",month="10",year="2019")
print(timesince)

# past date
past_date = pybengali.past_date('2')
print(past_date)

# future date
future_date = pybengali.future_date('2')
print(future_date)

year = pybengali.get_year(day="04", month="10", year="2021")
print(year)

weekday = pybengali.get_weekday(day="04", month="10", year="2021")
print(weekday)

bengali_digit = pybengali.convert_e2b_digit("10")
print(bengali_digit)

bengali_name = pybengali.eng_month_to_bengali("1")
print(bengali_name)

numbers = pybengali.bengali_numbers()
print(numbers)

months = pybengali.bengali_months()
print(months)

weekdays = pybengali.bengali_weekdays()
print(weekdays)

seasons = pybengali.bengali_seasons()
print(seasons)