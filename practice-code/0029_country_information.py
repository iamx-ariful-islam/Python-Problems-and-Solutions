# pip install countryinfo

from countryinfo import CountryInfo


# find all information about country
def find_info(country):
    print('Capital is    :', country.capital())
    print('Currencies is :', country.currencies())
    print('Languages is  :', country.languages())
    print('Borders are   :', country.borders())
    print('Others names  :', country.alt_spellings())

# root
if __name__ == '__main__':
    count = input('Enter your country: ')
    country = CountryInfo(count)
    find_info(country)