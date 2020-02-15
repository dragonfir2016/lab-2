import folium

map = folium.Map(location=[49.817545, 24.023932],
                 zoom_start=17)
map.add_child(folium.Marker(location=[49.817545, 24.023932],
                            popup="Хіба я тут!",
                            icon=folium.Icon()))

map.save('Map_3.html')