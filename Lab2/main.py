from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
import pandas
import geocoder
import reverse_geocoder

def find_films_year(path, year):
    """
    str -> ...
    Function takes path to file anf returns ...
    """
    answer = []
    with open(path, mode='r') as file:
        for line in file:
            line = line.replace('(TV)', '').replace('(V)', '').replace('(', '|').replace(')', '|').split('|')
            if line[1] == year:
                answer.append(line[2].replace('\t', '').strip())
    return set(answer)


def map_generator(latt, long, coords):
    """
    (int, int, list) -> None
    """
    m = folium.Map(location=[latt, long], zoom_start=10)
    
    tooltip = 'Клацни мем'
    for point in coords:
        folium.Marker([point[0], point[1]], popup='LGBT', tooltip=tooltip).add_to(m)
 
    m.save('map.html')



def main():
    year = input('Please enter a year you would like to have a map for: ').strip()
    lat, lng = input('Please enter your location (format: lat, long): ').split(',')
    print('Working on your map...')
    addresses = find_films_year('locations.list', year)

    print('Few more seconds...')
    final_locations = []

    location_cod = reverse_geocoder.search((lat, lng))
    loc_decoded = list(location_cod[0].items())
    for loc_txt in addresses:
        #print(loc_txt)
        if loc_decoded[2][1] in loc_txt or loc_decoded[3][1] in loc_txt or loc_decoded[4][1] in loc_txt and loc_decoded[4][1] != '':
            final_locations.append(loc_txt)
    #print(final_locations)
    
    geolocator = Nominatim(user_agent="specify_your_app_name_here")

    final_loc_coords = []
    for point in final_locations:
        coordinates = geolocator.geocode(point)
        final_loc_coords.append((coordinates.latitude, coordinates.longitude))
        
    print(final_loc_coords)

    map_generator(lat, lng, final_loc_coords)

    print('Finished.Your map: ')


if __name__ == "__main__":
    main()
    