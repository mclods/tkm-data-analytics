import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from numpy import random

# Merging Datasets(Basically DataFrames)
# Merging Datasets on Columns

# many to one merging
dframe1=DataFrame({'reference':['ola','uber','lyft','gojek','grab'],'revenue':[1,2,3,4,5]})
dframe2=DataFrame({'reference':['ola','uber','uber','ola'],'revenue':[1,2,3,4]})

print(dframe1)

print("*"*50)

print(dframe2)

print("*"*50)

df3=pd.merge(dframe1,dframe2)
print(df3)

print("*"*50)

df3=pd.merge(dframe1,dframe2,on='reference')
print(df3)

print("*"*50)

df4=pd.merge(dframe1,dframe2,on='reference',how='left')
print(df4)

print("*"*50)

df5=pd.merge(dframe1,dframe2,on='reference',how='outer')
print(df5)

print("*"*50)

df6=pd.merge(dframe1,dframe2,on='reference',how='right')
print(df6)

print("*"*50)

df7=DataFrame({'reference':['ola','ola','lyft','lyft','uber','uber','ola'],'revenue':[1,2,3,4,5,6,7]})
df8=DataFrame({'reference':['uber','uber','lyft','ola','ola'],'revenue':[1,2,3,4,5]})

print(df7)

print("*"*50)

print(df8)

print("*"*50)

print(pd.merge(df7,df8))

print("*"*50)

# Many References
df9=DataFrame({'reference':['ola','ola','lyft'],'revenue':['one','two','three'],'profit':[1,2,3]})
df10=DataFrame({'reference':['ola','ola','lyft','lyft'],'revenue':['one','one','one','three'],'profit':[4,5,6,7]})
print(pd.merge(df9,df10,on=['reference','revenue'],how='outer',suffixes=('_first','_second')))

print("*"*50)

# Merging based on Indexes
df1=DataFrame({'reference':['O','U','L','O','U'],'data':range(5)})
df2=DataFrame({'profit':[10,20]},index=['O','U'])

print(df1)

print("*"*50)

print(df2)

print("*"*50)

print(pd.merge(df1,df2,left_on='reference',right_index=True))   # Use left dataframe 'reference' and right dataframe index for merging

print("*"*50)

df3=DataFrame({'ref1':['A','A','O','O','A'],'ref2':[5,10,15,20,25],'ref3':[0,1,2,3,4]})
df4=DataFrame(np.arange(10).reshape(5,2),index=[['A','A','O','O','O'],[20,10,10,10,20]],columns=['col1','col2'])

print(df3)

print("*"*50)

print(df4)

print("*"*50)

print(pd.merge(df3,df4,left_on=['ref1','ref2'],right_index=True))

print("*"*50)

# Join Function
df3=DataFrame({'ref1':['A','A','A','O','O'],'ref2':[5,10,15,20,25],'ref3':np.arange(5.)})
df4=DataFrame({'ref1':['A','A','A','O','O'],'ref2':[15,20,25,30,35],'ref3':[2,3,4,5,6]})

print(df3.join(df4,lsuffix='x',rsuffix='y'))

print("*"*50)

# Concatenating Numpy Arrays
B1=np.arange(25).reshape(5,5)
A1=random.randn(25).reshape(5,5)

print(B1)

print("*"*50)

print(A1)

print("*"*50)

print("Output for Axis - 1")
print(np.concatenate([A1,B1],axis=1))   # Axis - 0 Row, Axis - 1 Column

print("*"*50)

print("Output for Axis - 0")
print(np.concatenate([A1,B1],axis=0))

print("*"*50)

# Concatenating Series
s1=Series([100,200,300],index=['A','B','C'])
s2=Series([400,500],index=['D','E'])

print("Axis 0")
print(pd.concat([s1,s2]))

print("*"*50)

print("Axis 1")
print(pd.concat([s1,s2],axis=1))

print("*"*50)

# Concatenating DataFrames
df1=DataFrame(random.rand(4,3),columns=['A','B','C'])
df2=DataFrame(random.rand(3,3),columns=['B','D','A'])

print("Axis 0")
print(pd.concat([df1,df2],sort=False))

print("*"*50)

print("Axis 0 - Continuous Index")
print(pd.concat([df1,df2],ignore_index=True,sort=False))

print("*"*50)


