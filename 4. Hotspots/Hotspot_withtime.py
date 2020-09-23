import folium
import pandas as pd
from folium import plugins

    
def hotspot_withtime(hmap_data, dates):    
    hmap = folium.Map(location = ['38.9','-77'], #Latitude and Longitude of line (Northing, Easting)
                      zoom_start = 11,  # Initial zoom level for the map.
                      tiles = 'OpenStreetMap',  #Map tileset to use.
                      control_scale = True)#Whether to add a control scale on the map.
    hm = folium.plugins.HeatMapWithTime(data = hmap_data, #list of list of points of the form [lat, lng] or [lat, lng, weight]
                                        index = list(dates), #Index giving the label (or timestamp) of the elements of data
                                        max_opacity = 0.6, #The maximum opacity for the heatmap
                                        min_opacity = 0, #The minimum opacity the heat will start at
                                        radius = 8, #Radius of each “point” of the heatmap
                                        auto_play = True, #Automatically play the animation across time.
                                        display_index = True) #Zoom level where the points reach maximum intensity (as intensity scales with zoom)
    hmap.add_child(hm)
    hmap.save(output_file)    


def read_data():
    df = pd.read_csv(input_file, sep=',')
    df = df.loc[df['Crime']==crime_type]
    
    hmap_data = []
    df['Date'] = [date[:8] for date in df['Date']]
    dates = df['Date'].unique()
    for date in dates:
        df_day = df.loc[df['Date']==date]
        data = [[row['X'], row['Y']] for index, row in df_day.iterrows()]
        hmap_data.append(data)
    return(hmap_data, dates)


if __name__ == '__main__':
    input_file = './data/dc-washington.csv'
    output_file = './html/dc-washington-time.html'
    crime_type = 'Burglary'
    
    hmap_data, dates = read_data()
    hotspot_withtime(hmap_data, dates)