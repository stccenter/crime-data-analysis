import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


#devide ann value according to P-value
def seperate_data(df):
    data, ps = list(df['ANN']), list(df['P_value'])
    x1, data1, x2, data2 = [], [], [], []
    for (i,ann), p in zip(enumerate(data), ps):
        if p<=0.05:
            data1.append(ann)
            x1.append(i)
        else:
            data2.append(ann)
            x2.append(i)
    return x1, data1, x2, data2


def BarChart(x1, data1, x2, data2, dates):
    mpl.rcParams["font.sans-serif"] = ["Times New Roman"]
    plt.figure(figsize=(8,4))
    
    plt.bar(x1, data1, edgecolor="peru", color="white", hatch="+++", label='ANN(P<=0.05)', width=1.0)    
    plt.bar(x2, data2, edgecolor="royalblue", color="white", hatch="/////", label='ANN(P>0.05)', width=1.0)    
           
    xticks = [date[5:7] + date[-2:].replace('/','0') for date in dates]
    yticks = np.arange(0, 2.1, 0.5)
    
    plt.xticks(np.arange(len(dates)), xticks, size=18, rotation=90)
    plt.yticks(yticks, size = 18)
    
    plt.xlabel("Date", fontdict={'size': 18})
    plt.ylabel("ANN", fontdict={'size': 18})
    
    plt.axhline(y=1, ls="--", c="lightgray")    
    plt.legend(loc="upper right", fontsize=16)
    plt.show()


def main():
    df = pd.read_csv(input_file, sep=',')
    dates = list(df['Date'].unique())
    
    x1, data1, x2, data2 = seperate_data(df)
    BarChart(x1, data1, x2, data2, dates)
    
    
if __name__ == '__main__':
    input_file = './result/ann-dc-washington.csv'    
    
    main()
