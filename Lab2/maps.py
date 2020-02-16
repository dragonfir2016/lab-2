import folium
#map.add_child(folium.Marker(location=[49.817545, 24.023932],popup="Хіба я тут!"))
#
#
#
#for lt, ln in zip(lat, lon):
# fg.add_child(folium.Marker(location=[lt, ln], popup="1900 рік", icon=folium.Icon()))
#map.add_child(fg)
#
#map.save('m.html')


def map_generator(latt, long, coords):
    """
    (int, int, list) -> None
    """
    m = folium.Map(location=[latt, long], zoom_start=10)
    
    tooltip = 'Click me'
    layer_2 = folium.FeatureGroup(name='Main')
    for point in coords:
        folium.Marker([point[0], point[1]], popup='Film was filmed there', tooltip=tooltip, icon=folium.Icon()).add_to(layer_2)
    folium.Marker([latt, long], popup='You are here', tooltip='Your location', icon=folium.Icon()).add_to(layer_2)

    layer_3 = folium.FeatureGroup(name="Population")
    layer_3.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

    m.add_child(layer_2)
    m.add_child(layer_3)
    m.add_child(folium.LayerControl())
    m.save('maps_%s.html' % '2000')
    return 

#map_generator(40.730610, -73.935242, [(40.6701033, -73.9859723), (40.6399951, -74.1376463), (43.309941, -73.644447), (40.765029999999996, -73.97988681588421)])
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
def locations_to_coords(locations):
    """
    list -> list
    Function takes list of locations and returns list of coordinates.
    >>> locations_to_coords(['Lviv'])
    [(49.841952, 24.0315921)]
    """
    coords_final = []

    coords_range = 9 if len(locations) >= 10 else len(locations)

    for point in range(coords_range):
        coordinates = geolocator.geocode(locations[point])
        if coordinates != None:
            coords_final.append((coordinates.latitude, coordinates.longitude))
    return coords_final

import doctest
doctest.testmod()