import phonenumbers
import folium
from myNumber import number
from phonenumbers import geocoder
from phonenumbers import carrier

# Create an account in https://opencagedata.com/
# Go to API Keys and add that key below
Key ='' # Enter your API Key here

num = phonenumbers.parse(number)

# get country location
yourLocation = geocoder.description_for_number(num, "en")
print(yourLocation)

# get service provider
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

# get location in map
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)

results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
#print(lat,lng)

myMap = folium.Map(location = [lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup = yourLocation).add_to((myMap))

# save map in html file
myMap.save("myLocation.html")