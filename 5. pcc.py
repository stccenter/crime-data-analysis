import pandas as pd
from scipy.stats import pearsonr

input_file = './Factors.csv'
x = 'population density'
y = 'diversity index'

df = pd.read_csv(input_file, sep=',')
pearsonr(df[x], df[y])