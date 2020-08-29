import pandas as pd

excelfile=pd.ExcelFile('sampleworksheet.xlsx')
dframe1=excelfile.parse('Sheet1')
dframe2=excelfile.parse('Sheet2')
dframe3=excelfile.parse('Sheet3')
dframe4=excelfile.parse('Sheet4')
dframe5=excelfile.parse('Sheet5')
dframe6=excelfile.parse('Sheet6')
dframe7=excelfile.parse('Sheet7')
dframe8=excelfile.parse('Sheet8')
dframe9=excelfile.parse('Sheet9')
dframe10=excelfile.parse('Sheet10')

print(dframe1)

print("*"*50)

print(dframe2)

print("*"*50)

print(dframe3)

print("*"*50)

print(dframe4)

print("*"*50)

print(dframe5)

print("*"*50)

print(dframe6)

print("*"*50)

print(dframe7)

print("*"*50)

print(dframe8)

print("*"*50)

print(dframe9)

print("*"*50)

print(dframe10)

dframe1.to_csv('csv1.csv',sep=',')
dframe2.to_csv('csv2.csv',sep=',')
dframe3.to_csv('csv3.csv',sep=',')
dframe4.to_csv('csv4.csv',sep=',')
dframe5.to_csv('csv5.csv',sep=',')
dframe6.to_csv('csv6.csv',sep=',')
dframe7.to_csv('csv7.csv',sep=',')
dframe8.to_csv('csv8.csv',sep=',')
dframe9.to_csv('csv9.csv',sep=',')
dframe10.to_csv('csv10.csv',sep=',')