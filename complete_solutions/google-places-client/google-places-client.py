import googlemaps
from datetime import datetime
from api_key_reader import read_key_from_file

# TODO:
# read API key from file
# main
# menu
# requests to new Places API
# update .gitignore file

def fetch_api_key():
    api_key = read_key_from_file("api_key.txt")
    return api_key


def fetch_geocode_info(gmaps):
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')


def fetch_paces_info():
    result = gmaps.places('Italian, Gothenburg, Sweden')

def fetch_place_info():
    result = gmaps.place('ChIJLURKSHbzT0YR9DuLi1AyS-I')

def fetch_specific_place_info(gmaps):
    list = []
    list.append('place_id')
    list.append('name')
    list.append('adr_address')
    list.append('wheelchair_accessible_entrance')
    result = gmaps.place(place_id='ChIJQS6xgGTzT0YRJaRvWxfYmAM', fields=list)
    print(result)


if __name__ == '__main__':
    print("Simple Google Places Client")
    gmaps = googlemaps.Client(key=fetch_api_key())
    fetch_specific_place_info(gmaps)

