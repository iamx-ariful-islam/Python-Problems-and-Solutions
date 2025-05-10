# pip install geopy

from geopy.geocoders import Nominatim


# create the geolocator object with a user-agent
geolocator = Nominatim(user_agent="geoapiExercises")

# get the city name from the user
city_name = input("Enter Your City Name: ")

# geocode of the location
location = geolocator.geocode(city_name)

print("Your Location: ", location)