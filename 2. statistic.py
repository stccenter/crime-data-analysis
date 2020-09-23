import pandas as pd


input_file = './Crime events 2020/dc-washington.csv'
output_file = './Crime number statistics 2020/dc-washington.csv'

daily_num = []    
headers = ['Name','Date','Total','Arrest','Arson','Assault','Burglary',
           'Robbery','Shooting','Theft','Vandalism','Other']
df = pd.read_csv(input_file, sep=',')
df['Date'] = [date[:8] for date in df['Date']]
dates = df['Date'].unique()        
county_name = df['Name'].unique()[0]
for date in dates:
    day_df = df.loc[df['Date'] == date]
    row = [county_name, date, len(day_df)]
    for crime_type in headers[3:]:        
        row.append(len(day_df.loc[day_df['Crime'] == crime_type]))
    daily_num.append(row)        

data_dir = {h:v for h,v in zip(headers, zip(*daily_num))}
outputdata = pd.DataFrame(data_dir)
outputdata.to_csv(output_file, sep=',', index=False, header=True)
