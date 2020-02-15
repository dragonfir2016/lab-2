import folium
map = folium.Map( location=[49.817545, 24.023932], zoom_start=17)
map.add_child(folium.Marker(location=[49.817545, 24.023932],popup="Хіба я тут!"))


fg = folium.FeatureGroup(name=”Kosiv map”)
for lt, ln in zip(lat, lon):
 fg.add_child(folium.Marker(location=[lt, ln],
 popup="1900 рік"
icon=folium.Icon()))
map.add_child(fg)
map.save('Map_5.html')

map.save('m.html')
