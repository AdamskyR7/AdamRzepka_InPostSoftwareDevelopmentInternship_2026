import pandas as pd
import folium
from folium.plugins import FastMarkerCluster

def generateMap(df: pd.DataFrame, fileName: str = "PaczkomatMap.html"):

    df = df.dropna(subset=['location.latitude', 'location.longitude'])

    center_lat = df['location.latitude'].mean()
    center_lon = df['location.longitude'].mean()

    fMap = folium.Map(location=[center_lat, center_lon], zoom_start=5, tiles='CartoDB positron')

    name = df['name'].fillna('')
    street =df['address_details.street'].fillna('')
    building_number = df['address_details.building_number'].fillna('')
    post_code = df['address_details.post_code'].fillna('')
    city = df['address_details.city'].fillna('')

    df['popup_text'] = name + " - " + street + " " + building_number + ", " + post_code + " " + city

    df['popup_text'] = df['popup_text'].str.replace(r"[\"\'\n\r]", " ", regex=True)

    usefuldata = df[['location.latitude', 'location.longitude', 'popup_text']].values.tolist()

    js_callback = """
    function (row) {
        var marker = L.circleMarker(new L.LatLng(row[0], row[1]), {
            radius: 10,
            color: '#FFFFFF',
            fillColor: '#FFCB00',
            fillOpacity: 0.8
        });
        if (row[2]){
            marker.bindPopup(row[2]);
        }
        return marker;
    }
    """

    FastMarkerCluster(data=usefuldata,callback=js_callback,name="Paczkomaty").add_to(fMap)

    fMap.save(fileName)
    print(f"Saved map to {fileName}")