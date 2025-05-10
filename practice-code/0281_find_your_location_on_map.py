# pip install geopy
# pip install folium

import folium
from geopy.geocoders import Nominatim


geolocator  = Nominatim(user_agent='my_geocoder_app')
map_address = input('Enter an address to map: ')

location    = geolocator.geocode(map_address)
if location:
    lat, lon = location.latitude, location.longitude
else:
    print('Address not found. Defaulting to white house')
    lat, lon = 38.8977, -77.0365
    
map_show = folium.Map(location=[lat, lon], zoom_start=15)
folium.Marker(
    location=[lat, lon],
    popup=f'{map_address}',
    icon=folium.Icon(color='blue')
).add_to(map_show)

map_show