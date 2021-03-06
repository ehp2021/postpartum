import pandas as pd
import folium
from folium import FeatureGroup
# from folium.plugins import MarkerCluster

#Create the base Map
m = folium.Map(location=[36.174465,-86.767960], tiles='OpenStreetMap', zoom_start=10)

#Read the data
df = pd.read_csv("obgyntn.csv")

#Create the markers
for i, row in df.iterrows():
    lat = df.at[i,'lat']
    lng = df.at[i,'lng']

    name = df.at[i,'name']
    service = df.at[i,'service']
    popup = df.at[i,'name'] +'<br>' + str(df.at[i,'service']) +'<br>' + str(df.at[i, 'street']) +'<br>' + str(df.at[i, 'zip'])

    if service == 'obgyn':
        color = 'blue'
    else:
        color = 'red'

    folium.Marker(location=[lat, lng],popup=popup, icon=folium.Icon(color=color)).add_to(m)

m.save("index.html")