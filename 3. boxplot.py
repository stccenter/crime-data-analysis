import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
    

def boxplot(crime_list):
    mpl.rcParams["font.sans-serif"] = ["Times New Roman"]
    plt.figure(figsize=(12, 5))
    
    plt.boxplot(x = crime_list, 
                patch_artist=True,
                showmeans=True, 
                widths = 0.85,
                boxprops = {'color':'black', 'facecolor':'steelblue'}, 
                flierprops = {'marker':'o','markerfacecolor':'brown','markeredgecolor':'brown', 'markeredgewidth':.1, 'markersize':3}, 
                meanprops = {'marker':'D','markerfacecolor':'indianred', 'markersize':4},
                medianprops = {'linestyle':'-','color':'orange'})
    x_loc = np.arange(0, len(crime_list)+1, 1)
    plt.xticks(x_loc, x_loc, size=12)
    plt.yticks(size=14)
    plt.xlabel('County/City id', size=14)
    plt.ylabel('Crime rate per 10,000 people', size=14)
    plt.grid(linestyle="--", alpha=0.3)
    #plt.title('Crime Rate for Counties/Cities', size=18)
    plt.show()


# read population data
def read_pop():
    pop_dir = {}
    factor_df = pd.read_csv(pop_file, sep=',')
    pop_list = list(factor_df['Total population'])
    city_list = list(factor_df['Name'])
    for pop, city in zip(pop_list,city_list):
        pop_dir[city] = pop
    return pop_dir


def main():
    pop_dir = read_pop()
    
    crime_list = []
    file_list = os.listdir(input_path)
    file_list.sort()
    for file_name in file_list:       
        population = pop_dir[file_name[:-4]]        
        df = pd.read_csv(input_path + file_name)
        df['Total'] = df['Total']-df['Arrest']-df['Other']        
        df['Rate'] = df['Total']/population*10000
        crime_list.append(df['Rate'])        
    
    # ranking from low to high based on median of crime rate
    median_list = [np.median(num) for num in crime_list]
    sort_id = np.argsort(median_list)
    crime_list = [crime_list[i] for i in sort_id]
    county_list = [file_list[i][:-4] for i in sort_id]
    
    for i in range(len(county_list)):
        print(i+1, ';', np.mean(crime_list[i]), ';', county_list[i])    
    boxplot(crime_list)
    

if __name__ == '__main__':
    input_path = './Crime number statistics 2020/'
    pop_file = './Factors.csv'
        
    main()    