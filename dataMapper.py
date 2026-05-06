import pandas as pd
import folium
from folium.plugins import FastMarkerCluster

def generateMap(df: pd.DataFrame, fileName: str = "PaczkomatMap.html"):

    df = df.dropna(subset=['location.latitude', 'location.longitude'])

    df = df[df['country'] == 'PL']

    center_lat = df['location.latitude'].mean()
    center_lon = df['location.longitude'].mean()

    fMap = folium.Map(location=[center_lat, center_lon], zoom_start=5, tiles='CartoDB positron')

    usefuldata = df[['location.latitude', 'location.longitude']].values.tolist()

    cluster = FastMarkerCluster(data=usefuldata,name="Paczkomaty").add_to(fMap)

    # for index, row in df.iterrows():
    #     lat = row['location.latitude']
    #     lon = row['location.longitude']
    #     name = row['name']
    #     address = f"{row['address_details.street']} {row['address_details.building_number']}, {row['address_details.post_code']}, {row['address_details.city']}"
    #
    #     folium.CircleMarker(
    #         location=[lat, lon],
    #         popup=f'{name} - {address}'#,
    #         #icon=folium.Icon()
    #     ).add_to(cluster)



    fMap.save(fileName)
    print(f"Saved map to {fileName}")