import pandas as pd

input_file = './Factors.csv'
output_file = './pcc.csv'

df = pd.read_csv(input_file, sep=',')
variables = list(df.columns)[3:]
x = df[variables]
corrs = x.corr(method='pearson')
corrs.to_csv(output_file, sep=',', index=False, header=True)