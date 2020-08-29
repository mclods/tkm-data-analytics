import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

series1=Series([10,20,30,40],index=['a','b','c','d'])

# Index List
index1=series1.index
print(index1)

print("*"*50)

print(index1[2:])

print("*"*50)

# Negative Indexes
print(index1[:-2])

print("*"*50)

# Range of Indexes
print(index1[2:3])

print("*"*50)

# Changing the Indexes
# index1[0]='e' --> This is not allowed

# Reindexing
series1=Series([1,2,3,4],index=['e','f','g','h'])
print(series1)

print("*"*50)

# Creating new indexes using reindex()
series2=series1.reindex(['e','f','g','h','i','j'])
print(series2)

print("*"*50)

# Using fillvalue
series2=series2.reindex(['e','f','g','h','i','j','k'],fill_value=10)
print(series2)

print("*"*50)

# Using reindex methods -<ffill
cars=Series(['Audi','Mercedes','BMW'],index=[0,4,8])
print(cars)

print("*"*50)

ranger=range(13)
print(ranger)

print("*"*50)

cars=cars.reindex(ranger,method="ffill") # ffill --> forward fill
print(cars)

print("*"*50)

# Create new DataFrame from randn
df_1=DataFrame(randn(25).reshape(5,5),index=['a','b','c','d','e'],columns=['c1','c2','c3','c4','c5'])
print(df_1)

print("*"*50)

# reindex rows
df_2=df_1.reindex(['a','b','c','d','e','f'])
print(df_2)

print("*"*50)

# reindex columns
df_3=df_1.reindex(columns=['c1','c2','c3','c4','c5','c6'])
print(df_3)

print("*"*50)

# Using .ix[] to reindex
# df_4=df_1.ix[['a','b','c','d','e','f'],['c1','c2','c3','c4','c5','c6']] --> Deprecated
# print(df_4)

# print("*"*50)

# Selecting and Modifying Entries
series1=Series([100,200,300],index=['A','B','C'])
print(series1)

print("*"*50)

print(series1['A'])
print(series1['B'])

print("*"*50)

print(series1[['A','B']])

print("*"*50)

# Numeric Indexes
print(series1[0])
print(series1[0:2])

print("*"*50)

# Conditional Indexes
print(series1[series1>150])
print(series1[series1==300])

print("*"*50)

df1=DataFrame(np.arange(9).reshape(3,3),index=['car','bike','cycle'],columns=['A','B','C'])
print(df1)

print("*"*50)

print(df1['A'])
print(df1[['A','B']])

print("*"*50)

print(df1>5)

print("*"*50)

# ix function access
# print(df1.ix['bike'])
# print(df1.ix[1])

# print("*"*50)

# Data Alignment
ser_a=Series([100,200,300],index=['a','b','c'])
ser_b=Series([100,200,300,400],index=['a','b','c','d'])

# Sum of Series
print(ser_a+ser_b)

print("*"*50)

# Sum of DataFrames
df1=DataFrame(np.arange(4).reshape(2,2),columns=['a','b'],index=['car','bike'])
df2=DataFrame(np.arange(9).reshape(3,3),columns=['a','b','c'],index=['car','bike','cycle'])
print(df1)
print(df2)

print("*"*50)

print(df1+df2)

print("*"*50)

# Filling NaN values
df1=df1.add(df2,fill_value=0)
print(df1)

print("*"*50)

# Access Columns
# ser_c=df2.ix[0]
# print(df2-ser_c)

# print("*"*50)

# Ranking - Sorting
ser1=Series([500,1000,1500],index=['a','c','b'])
print(ser1)

print("*"*50)

# Sorting takes place according to rank
# Sorting by index
print(ser1.sort_index())

print("*"*50)

# Sort by values
print(ser1.sort_values())

print("*"*50)

print(ser1.rank())

print("*"*50)

# Ranking of Series
ser2=Series(randn(10))
print(ser2)

print("*"*50)

print(ser2.rank())

print("*"*50)

ser2=ser2.sort_values()
print(ser2.rank())

print("*"*50)

# Pandas Statistics
array1=np.array([[10,np.nan,20],[30,40,np.nan]])
print(array1)

print("*"*50)

df1=DataFrame(array1,index=[1,2],columns=list('ABC'))
print(df1)

print("*"*50)

# sum() --> Sums along each column
print(df1.sum(axis=1)) # sum along indexes

print("*"*50)

# Min Max along columns
print(df1.min())

print("*"*50)

print(df1.max())

print("*"*50)

# Index having maximum values
print(df1.idxmax())

print("*"*50)

# Cummulative Sum
print(df1.cumsum())

print("*"*50)

# Get a description
print(df1.describe())

print("*"*50)

# Plotting the DataFrame
df2=DataFrame(randn(9).reshape(3,3),index=[1,2,3],columns=list("ABC"))
print(df2)

print("*"*50)

plt.plot(df2)
plt.legend(df2.columns,loc="lower right")
plt.savefig('samplepic.png')
# plt.show()

# Unique Values
ser1=Series(list('abcccaabd'))
print(ser1.unique())

print("*"*50)

# Frequency of elements
print(ser1.value_counts())