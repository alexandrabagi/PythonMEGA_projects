import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """<h4>Volcano information:</h4>
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation >= 1000 and elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[37.737123, -122.441136], zoom_start=6, tiles="Stamen Terrain")

fg_v = folium.FeatureGroup(name="Volcanoes")
fg_p = folium.FeatureGroup(name="Population")

for lt, ln, el, n in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html=html % (n,n,el), width=200, height=100)
    fg_v.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), fill=True, fill_color=color_producer(el), color='black', opacity=0.5, fill_opacity=0.7)) # popup=folium.Popup(str(el), parse_html=True)

fg_p.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
else 'red'}))

map.add_child(fg_v)
map.add_child(fg_p)

map.add_child(folium.LayerControl())

map.save("MyMap.html")