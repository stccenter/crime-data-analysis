import folium
import pandas as pd
from folium import plugins


def hotspot(hmap_data):
    hmap = folium.Map(location = ['38.9','-77'], #Latitude and Longitude of Map (Northing, Easting).
                      zoom_start = 11,  # Initial zoom level for the map.
                      tiles = 'OpenStreetMap',  #Map tileset to use.
                      control_scale = True) #Whether to add a control scale on the map.
    hm = folium.plugins.HeatMap(data = hmap_data, #list of points of the form [lat, lng] or [lat, lng, weight]
                                max_val = 10, #Maximum point intensity
                                min_opacity = 1, #The minimum opacity the heat will start at
                                radius = 6, #Radius of each “point” of the heatmap
                                blur = 10, #Amount of blur
                                gradient = {0:'lightblue', 0.3:'blue', 0.6: 'yellow', 1: 'red'}, #Color gradient config
                                max_zoom = 2) #Zoom level where the points reach maximum intensity (as intensity scales with zoom)
    hmap.add_child(hm)
    hmap.save(output_file)
    

def read_data():
    df = pd.read_csv(input_file, sep=',')
    df_day = df.loc[df['Date']==date]
    for_map = df_day.loc[df_day['Crime']==crime_type]
    hmap_data = [[row['X'], row['Y']] for index, row in for_map.iterrows()]
    return(hmap_data)


if __name__ == '__main__':
    input_file = './data/dc-washington.csv'
    output_file = './html/dc-washington.html'
    date = '05/31/20'
    crime_type = 'Burglary'
    
    hmap_data = read_data()
    hotspot(hmap_data)