import pandas as pd

df = pd.read_excel("Simulation plan.xlsx")
print(df.head())
'''
# the itertuples cannot specify the range of the rows, instead it will 
# loop all rows in the dataframe
for row in df.itertuples(index=False):
	print(row)
	print('meshsize = ', row[1])
'''
print(df.shape)	
print(df.sh)
#for index in range(1,len(df))
