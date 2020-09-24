import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


def line_chart(data, city_name, dates):    
    mpl.rcParams["font.sans-serif"] = ["Times New Roman"]
    plt.figure(figsize=(12, 8))
    
    colors = ["gold", "peru",  "navy", "lightcoral", "teal", "brown", "skyblue"]
    markers = ['o', '*', 'd', 'h', '.', '^', 's', '+', 'x']
    
    x_loc = np.arange(0, len(dates), 1)
    for crime_type in data:
        i = crime_types.index(crime_type)
        plt.plot(x_loc, data[crime_type], marker=markers[i], markersize=5, color=colors[i], mec=colors[i], mfc=colors[i],label=crime_type)
        
    x_ticks = [date[:5] for date in dates]
    plt.xticks(x_loc, x_ticks, size=18, rotation=90)
    
    max_value = (int(max([max(data[i]) for i in data])/10)+1)*10    
    grad = (int(max_value/50)+1)*10
    y_loc = np.arange(0, max_value+grad, grad)
    plt.yticks(y_loc, y_loc, size=18)
    
    plt.xlabel('Date', size=18)
    plt.ylabel('Number of Crimes', size=18)
        
    plt.legend(loc="upper left", fontsize=14)
    plt.savefig(output_path+city_name+'.jpg')
    plt.close()
    

def main():
    file_list = os.listdir(input_path)
    file_list.sort()        
    for filename in file_list:
        crime_num_dic = {}
        df = pd.read_csv(input_path + filename, sep=',')        
        dates = [date for date in df['Date'] if date>='05/15/20']        
        city_name = filename[3:-4].replace('+',' ').title() + ', ' + filename[:2].upper()        
        for crime_type in crime_types:
            crime_num = [num for date,num in zip(df['Date'],df[crime_type]) if date>='05/15/20']
            crime_num_dic[crime_type] = crime_num
        line_chart(crime_num_dic, city_name, dates)
    

if __name__ == '__main__':
    input_path = './Crime number statistics 2020/'
    output_path = './result/'
    
    crime_types = ['Arson', 'Assault', 'Burglary', 'Robbery', 'Shooting', 'Theft', 'Vandalism']
    
    main()