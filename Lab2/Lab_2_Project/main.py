from geopy.geocoders import Nominatim
import folium
import reverse_geocoder


def find_films_year(path, year):
    """
    str -> set
    Function takes path to file anf returns set of films locations.
    """
    answer = []
    with open(path, mode='r') as file:
        for line in file:
            line = line.replace('(TV)', '').replace('(V)', '')
            line = line.replace('(', '|').replace(')', '|').split('|')
            if line[1] == year:
                answer.append(line[2].replace('\t', '').strip())
    return set(answer)


def find_near_locations(latt, long, places):
    """
    (str, str, set) -> list
    Function takes user location and returns list of nearest film making
    locations.
    """
    final_locations = []

    user_location = list(reverse_geocoder.search((latt, long))[0].items())
    for loc_txt in places:
        if user_location[2][1] in loc_txt or user_location[3][1] in loc_txt or\
        user_location[4][1] in loc_txt and user_location[4][1] != '':
            final_locations.append(loc_txt)
    return final_locations


def map_generator(latt, long, coords, year):
    """
    (int, int, list) -> None
    Function takes lattitude and longitude of the user and returns map
    with the nearest location of films making.
    >>> map_generator(40.730610, -73.935242, [(40.6701033, -73.9859723)], 2002)

    """
    m = folium.Map(location=[latt, long], zoom_start=10)

    tooltip = 'Click me'
    layer_2 = folium.FeatureGroup(name='Main')
    for point in coords:
        folium.Marker([point[0], point[1]], popup='Film was filmed there',
                      tooltip=tooltip, icon=folium.Icon()).add_to(layer_2)
    folium.Marker([latt, long], popup='You are here', tooltip='Your location',
                  icon=folium.Icon()).add_to(layer_2)

    layer_3 = folium.FeatureGroup(name="Population")
    layer_3.add_child(folium.GeoJson(data=open('world.json', 'r',
        encoding='utf-8-sig').read(),
        style_function=lambda x: {'fillColor': 'green'
        if x['properties']['POP2005'] < 10000000 else 'orange'
            if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

    m.add_child(layer_2)
    m.add_child(layer_3)
    m.add_child(folium.LayerControl())
    m.save('map_%s.html' % year)


def locations_to_coords(locations):
    """
    list -> list
    Function takes list of locations and returns list of coordinates.
    >>> locations_to_coords(['Lviv'])
    [(49.841952, 24.0315921)]
    """
    coords_final = []
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    coords_range = 9 if len(locations) >= 10 else len(locations)

    for point in range(coords_range):
        coordinates = geolocator.geocode(locations[point])
        if coordinates is not None:
            coords_final.append((coordinates.latitude, coordinates.longitude))
    return coords_final


def main():
    """
    None -> File
    Main function of the module, creates map of films making locations
    based on the user coordinates.
    """
    year = input('Please enter a year you would like to have a map for: ')
    year = year.strip()
    lat, lng = input('Enter your location (format: lat, long): ').split(',')
    print('Working on your map...')

    films_addresses = find_films_year('locations.list', year)

    print('Few more seconds...')

    final_locations = find_near_locations(lat, lng, films_addresses)

    final_loc_coords = locations_to_coords(final_locations)

    map_generator(lat, lng, final_loc_coords, year)

    print("Finished.Your map: " + 'map_%s.html' % year)


if __name__ == "__main__":
    main()
