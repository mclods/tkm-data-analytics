import pandas as pd
from pandas import DataFrame,read_html

# In .csv the separator is comma but in .xlsx we have different separator.
# In .xlsx we can have multiple sheets of data whereas in .csv we have single sheet of data.

excelfile=pd.ExcelFile('demo2.xlsx')
dframe=excelfile.parse('Sheet1')    #Sheet Name
print(dframe)

print("*"*50)

# Handling HTML with pandas
# url="https://countrycode.org/"
# dflist=pd.io.html.read_html(url)
# dframe=dflist[0]
# print(dframe)

# print("*"*50)

# print(dframe.columns.values)
