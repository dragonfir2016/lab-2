import folium
import pandas

file_list = ["Stan_1900.csv", "Stan_1914.csv", "Stan_1938.csv"]

map = folium.Map(location=[48.314775, 25.082925],
                 zoom_start=10)
fg_list = []
for i in file_list:
    data = pandas.read_csv(i, error_bad_lines=False)
    lat = data['lat']
    lon = data['lon']
    churches = data['церкви']
    fg = folium.FeatureGroup(name=i)

    for lt, ln, ch in zip(lat, lon, churches):
        fg.add_child(folium.Marker(location=[lt, ln],
                                   popup="1900 рік"+"\n" + i,
                                   icon=folium.Icon()))
    fg_list.append(fg)

for i in fg_list:
    map.add_child(i)

map.add_child(folium.LayerControl())
map.save('Map_5.html')
