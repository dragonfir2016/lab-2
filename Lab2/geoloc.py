
import folium

m = folium.Map(location=[49.8350125, 24.0197128], zoom_start=12)

tooltip = 'Клацни мем'

folium.Marker([49.822994, 24.0353093], popup='свенца', tooltip=tooltip).add_to(m)
folium.Marker([49.8174143, 24.0216516], popup='бфк', tooltip=tooltip).add_to(m)

m.save('map.html')