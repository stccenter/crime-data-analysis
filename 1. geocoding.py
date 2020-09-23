import csv
import geocoder
import pandas as pd


input_file = './Crime events 2020/dc-washington.csv'
output_file = './Crime events with coordinates 20201/dc-washington.csv'
date = '05/15/20'

output = open(output_file, 'w', newline='')
csv_write = csv.writer(output, dialect='excel')
csv_write.writerow(['Name', 'Crime','Date','Address','X','Y'])

df = pd.read_csv(input_file, sep=',', encoding = "ISO-8859-1")
df['Day'] = [date[:8] for date in df['Date']]
day_df = df.loc[df['Day'] == date]
for item in day_df.iterrows():
    name, address, crime, date = item[1]['Name'], item[1]['Address'], item[1]['Crime'], item[1]['Date']        
    g = geocoder.arcgis(address)
    latitude, longitude = str(g.lat), str(g.lng)
    csv_write.writerow([name, crime, date, address, latitude, longitude])