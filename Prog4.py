import pandas as pd
from pandas import Series,DataFrame
import numpy as np

revenue_df=pd.read_clipboard()
print(revenue_df)

print("*"*50)

# Print Index and Columns
print(revenue_df.columns)
print(revenue_df['Rank'])

print("*"*50)

# Access Multiple Columns using DataFrame
print(DataFrame(revenue_df,columns=['Rank','Company','Market value']))

print("*"*50)

# NaN values
revenue_df2=DataFrame(revenue_df,columns=['Rank','Company','Market value','Loss'])
print(revenue_df2)

print("*"*50)

# Head and Tail Statements

# Head ->Prints the first specified entries of data
print(revenue_df.head(2))

print("*"*50)

# Tail ->:Prints the last two specified of data
print(revenue_df.tail(2))

print("*"*50)

# Access Rows of DataFrame
print(revenue_df.iloc[0])
print(revenue_df.iloc[5])

print("*"*50)

# Assigning values to DataFrame

# Using numpy
arr=np.array([1,2,3,4,5,6])
revenue_df2['Loss']=arr
print(revenue_df2)

print("*"*50)

# Using Series
arr=Series([900,1000],index=[3,5])
revenue_df2['Loss']=arr
print(revenue_df2)

print("*"*50)

# Deletion
del revenue_df2['Loss']
print(revenue_df2)

print("*"*50)

# Create DataFrame from Dictionary
sample={'Company':['A','B'],'Profit':[1000,5000]}
print(sample)

print("*"*50)

sample_df=DataFrame(sample)
print(sample_df)