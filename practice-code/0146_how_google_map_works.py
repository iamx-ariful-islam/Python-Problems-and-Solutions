import bisect


# set some default latitude and longitude
lati_long    = [[], [20.5937, 78.9629], [37.0902, 95.7129], [52.1326, 5.2913], [55.3781, 3.4360]]
# country list as default latitude and longitude
country_list = ['', 'India', 'USA', 'Netherlands', 'UK']

# find country using latitude and longitude
def google_map(arg):
    idx = bisect.bisect(lati_long, arg) - 1
    return f'Latitude {arg[0]}, Longitude {arg[1]} is {country_list[idx]}'


# calling function
print(google_map([55.3781, 3.4360]))


'''output:

Latitude 55.3781, Longitude 3.436 is UK
'''