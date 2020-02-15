import folium

map = folium.Map(location=[49.817545, 24.023932],
                 zoom_start=17)

fg = folium.FeatureGroup(name="Lviv_map")
fg.add_child(folium.Marker(location=[49.817545, 24.023932],
                            popup="Хіба я тут!",
                            icon=folium.Icon()))
map.add_child(fg)
map.save('Map_4.html')