import pandas as pd
import folium
from folium.plugins import FastMarkerCluster, HeatMap
import branca.colormap as cm


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

    coordinates_dict = pd.Series(zip(df['location.latitude'], df['location.longitude']), index=df['name']).to_dict()

    def changeNameToCoordinates(recs):
        targetCoordinates = []
        if isinstance(recs, list):
            for rec_name in recs:
                if rec_name in coordinates_dict:
                    targetCoordinates.append(coordinates_dict[rec_name])
        return targetCoordinates

    df['targetCoordinates'] = df['recommended_low_interest_box_machines_list'].apply(changeNameToCoordinates)

    useful_data = df[['location.latitude', 'location.longitude', 'popup_text', 'targetCoordinates']].values.tolist()

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
        
        if (row[3] && row[3].length > 0) {
            marker.on('popupopen', function(e) {
                var map = e.target._map;
                
                if (window.activeLines) {
                    window.activeLines.forEach(function(line) { map.removeLayer(line); });
                }
                window.activeLines = [];

                row[3].forEach(function(targetCoords) {
                    var line = L.polyline([ [row[0], row[1]], targetCoords ], {
                        color: 'red',
                        weight: 2,
                        dashArray: '5, 5'
                    }).addTo(map);
                    window.activeLines.push(line);
                });
            });

            marker.on('popupclose', function(e) {
                var map = e.target._map;
                if (window.activeLines) {
                    window.activeLines.forEach(function(line) { map.removeLayer(line); });
                    window.activeLines = [];
                }
            });
        }
        return marker;
    }
    """

    cluster_layer = folium.FeatureGroup(name="Paczkomaty", show=True)
    FastMarkerCluster(data=useful_data,callback=js_callback).add_to(cluster_layer)

    heatmap_data = df[['location.latitude', 'location.longitude']].values.tolist()

    heatmap_layer = folium.FeatureGroup(name="Heatmap", show=False)
    HeatMap(data=heatmap_data,name="Paczkomaty_MapaCiepla",min_opacity=0.7,max_zoom=1,radius=90,blur=45,show=True).add_to(heatmap_layer)

    cluster_layer.add_to(fMap)
    heatmap_layer.add_to(fMap)

    folium.LayerControl(collapsed=False).add_to(fMap)

    fMap.save(fileName)
    print(f"Saved map to {fileName}")