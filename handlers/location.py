import geocoder
from geopy.geocoders import Nominatim

g = None
geolocator = None

def init():
    global g, geolocator
    g = geocoder.ip('me')
    geolocator = Nominatim(user_agent="geoapiExercises")

def getLongLat():
    global g
    return g.latlng

def get_location(long, lat):
    global geolocator
    location = geolocator.reverse(long+","+lat)
    return location.address