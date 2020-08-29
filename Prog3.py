import pandas as pd
from pandas import Series
import numpy as np

# Pandas Series

# Use Series function
object=Series([5,10,15,20])
print(object)

print("*"*50)

# Print object without indexes
print(object.values)

print("*"*50)

# Print Indexes
print(object.index)

print("*"*50)

# Convert numpy arrays to Series
data_array=np.array(['a','b','c'])
s=Series(data_array)
print(s)

print("*"*50)

# Use custom indexes
s=Series(data_array,index=[100,101,102])
print(s)

print("*"*50)

s=Series(data_array,index=['index1','index2','index3'])
print(s)

print("*"*50)

# Real Life example
revenue=Series([10,20,30,40],index=['ola','uber','grab','gojek'])
print(revenue['ola'])
print(revenue[revenue>=35])
print('lyft' in revenue)

print("*"*50)

# Convert Series to dictionary
revenue_dict=revenue.to_dict()
print(revenue_dict)

print("*"*50)

# Having NaN values
index2=['ola','uber','grab','gojek','lyft']
revenue2=Series(revenue,index2)
print(revenue2)

print("*"*50)

# Check for null values
print(pd.isnull(revenue2))
print(pd.notnull(revenue2))

print("*"*50)

# Addition of Series (+)
print(revenue+revenue2)

print("*"*50)

# Assigning Names
revenue2.name="Company Revenues"
revenue2.index.name="Company Names"
print(revenue2)