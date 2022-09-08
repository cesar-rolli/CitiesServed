import pandas as pd
import folium
from geopy.geocoders import Nominatim
import time

# Served cities list
served_cities = ['Água Santa, Rio Grande do Sul', 'Agudo, Rio Grande do Sul', 'Ajuricaba, Rio Grande do Sul', 'Almirante Tamandaré do Sul, Rio Grande do Sul', 'Alpestre, Rio Grande do Sul', 'Alto Alegre, Rio Grande do Sul',
'Alto Feliz, Rio Grande do Sul', 'Alvorada, Rio Grande do Sul']

# Search latitude and longitude using GeoPy
latitude_list = []
longitude_list = []

for cities in served_cities:
  # Latitude
  geolocator = Nominatim(user_agent="geolocation")
  location = geolocator.geocode({cities})
  latitude_list.append(location.latitude)
  time.sleep(0.5)
  
  # Longitude
  geolocator = Nominatim(user_agent="geolocation")
  location = geolocator.geocode({cities})
  longitude_list.append(location.longitude)
  time.sleep(0.5)
  
# Create dictionary with list of served cities, latitude and longitude
cities_list = {}
cities_list['Cidades atendidas'] = served_cities[:]
cities_list['Latitude'] = latitude_list[:]
cities_list['Longitude'] = longitude_list[:]
  
# Transform dictionary (cities_list) to CSV
data = pd.DataFrame(data = cities_list).to_csv('cities_list.csv', index = False)

# Create the map from cities, latitude and longitude CSV
cities_served = pd.read_csv('cities_list.csv')
cities_served = cities_served[['Latitude', 'Longitude']]

# -30.0324999,-51.2303767 is the location of Porto Alegre, center of the map when opened
map = folium.Map(location=[-30.0324999,-51.2303767], zoom_start = 8, control_scale = True)

for index, location_info in cities_served.iterrows():
  folium.Marker([location_info['Latitude'], location_info['Longitude']]).add_to(map)
  map.save('map.html')