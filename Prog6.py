import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# csv file --> Commas Separated Values

# Considers 1st Row as the header
dframe=pd.read_csv('demo.csv')
print(dframe)

print("*"*50)

# Does not consider 1st Row as the header
dframe=pd.read_csv('demo.csv',header=None)
print(dframe)

print("*"*50)

# Use readtable --> We can use any separator other than commas as in csv
dframe2=pd.read_table('demo.csv',sep=',',header=None)
print(dframe2)

print("*"*50)

# Partial rows importing
print(pd.read_csv('demo.csv',nrows=2,header=None))

print("*"*50)

# Dump to csv
dframe2.to_csv('outputCSV.csv',sep='!')

# Dump specific Columns
dframe.to_csv('outputCSV1.csv',columns=[0,1])
