import folium
import pandas

#define new columns in d table by passing thr following:
ca= "cases"
print("cases")

de = "Deaths"
print("Deaths")


# use this to call up data to use as map
data = pandas.read_csv("Coronavirus_COVID-19_Cases_V21.txt")



lat = list(data["Lat"])
lon = list(data["Long_"])
cases = list(data["Confirmed"])
Deaths = list(data["Deaths"])

def color_producer(cases):
    if cases < 2000:
        return 'green'
    elif 2000 <= cases < 20000:
        return 'orange'
    else:
        return 'black'

map = folium.Map(location= [38.58, -99], zoom_start=6, tiles= "Stamen Terrain")

fg1 = folium.FeatureGroup(name= "Covid")

for  lt, ln,ca, de in zip(lat, lon, cases, Deaths ):
    fg1.add_child(folium.CircleMarker(location=[lt,ln],raduis = 6,popup="\n Cases:" +str(ca) + "\n Deaths:" +str(de) , fill_color = color_producer(ca), color ='grey', fill_opacity= 0.7 ))

fg2 = folium.FeatureGroup(name= "Population")

fg2.add_child(folium.GeoJson(data = open ('world.json','r', encoding='utf-8-sig').read(),style_function = lambda x: {'fillColor' : 'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' } ))


map.add_child(fg1)
map.add_child(fg2)

map.add_child(folium.LayerControl())

map.save("Map4.html")