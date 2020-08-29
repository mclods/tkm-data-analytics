import numpy as np

# Numpy Introduction

# Create a numpy array
my_list=[1,2,3,4]
my_array=np.array(my_list)
print(my_array)

print("*"*50)

# Create a multidimensional numpy array
my_list1=[1,2,3,4]
my_list2=[5,6,7,8]
my_m_array=np.array([my_list1,my_list2])
print(my_m_array)

print("*"*50)

# Print the dimensions of the array
print(my_m_array.shape)

print("*"*50)

# Print the datatype of the members of the array
print(my_m_array.dtype)

print("*"*50)

# Create an array of zeroes
new_array=np.zeros(5)
print(new_array)

print("*"*50)

# Create an array of ones
new_array=np.ones([5,5])
print(new_array)

print("*"*50)

# Create an empty array
new_array=np.empty(5)
print(new_array)

print("*"*50)

# Create an identity matrix
new_array=np.eye(5)
print(new_array)

print("*"*50)

# Create a range of numbers with start:stop:step
new_array=np.arange(5,50,2)
print(new_array)

print("*"*50)

# Perform Scalar Multiplication
array1=np.array([[1,2,3,4],[5,6,7,8]])
print(array1*array1)

print("*"*50)

# Perform Exponential Multiplication
print(array1**3)

print("*"*50)

# Perform Subtraction
print(array1-array1)

print("*"*50)

# Perform Reciprocal
print(1/array1)

print("*"*50)

# Indexing and Slicing
arr=np.arange(0,10)
print(arr)
print(arr[0])
print(arr[2])

print("*"*50)

arr2=arr[0:6]
print(arr2)

print("*"*50)

arr2[:]=12
print(arr2)

print("*"*50)

print(arr)  # arr2 has not been allocated separate space it's actually arr from 0:6 which gets modified as arr2[:]=12

print("*"*50)

# Creating a new Copy Array (Separate Memory Space Allocated)
arrcopy=arr.copy()
print(arrcopy)

print("*"*50)

# Indexing and Slicing Multidimensional Arrays
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)

print("*"*50)

print(arr2d[1])
print(arr2d[0][1])

print("*"*50)

print(arr2d[0:2,0:2])

print("*"*50)

# Using Loops with Array
for i in range(arr2d.shape[0]):
    arr2d[i]=i
print(arr2d)

print("*"*50)

# One way of accessing the rows
print(arr2d[[1,0]])

print("*"*50)

# Operations on Arrays
arr=np.arange(15)

# sqrt
print(np.sqrt(arr))

print("*"*50)

# exp
print(np.exp(arr))

print("*"*50)

# add
arr1=np.arange(15)
print(np.add(arr,arr1))

print("*"*50)

# max
arr=np.arange(15)
# print(np.max(arr,arr1))

# print("*"*50)

# Saving and Loading Arrays
arr=np.arange(10)
print(arr)

print("*"*50)

np.save('saved_array',arr)

new_array=np.load('saved_array.npy')
print(new_array)

print("*"*50)

# Saving Multiple Arrays
arr1=np.arange(25)
arr2=np.arange(30)

np.savez('saved_archive.npz',x=arr1,y=arr2)
new_array=np.load('saved_archive.npz')

print(new_array['x'])
print(new_array['y'])

print("*"*50)

# Save to text file
np.savetxt('textfile.txt',arr,delimiter=',')

# Load text file
load_txt=np.loadtxt('textfile.txt',delimiter=',')
print(load_txt)

print("*"*50)

# Boolean operations on numpy Array
x=np.array([100,200,300,400])
y=np.array([10,20,30,40])
condition=np.array([True,True,False,False])

# Using List Comprehensions
z=[a if cond else  b for a,b,cond in zip(x,y,condition)]
print(z)

print("*"*50)

# Using where condition
z2=np.where(condition,x,y)
print(z2)

print("*"*50)

z3=np.where(x>0,0,1)
print(z3)

print("*"*50)

# Some Standard Functions

# sum
print(x.sum())

print("*"*50)

# Column sum
print(x.sum(0))

print("*"*50)

# Mean
print(x.mean())

print("*"*50)

# Standard Deviation
print(x.std())

print("*"*50)

# Variance
print(x.var())

print("*"*50)

# Logical Operations ->and & or
condition=np.array([True,False,True])

print(condition.any())  #or operator
print(condition.all())  #and operator

print("*"*50)

# Sorting a numpy Array
unsorted_array=np.array([1,2,8,10,7,3])
unsorted_array.sort()
print(unsorted_array)

print("*"*50)

# Finding unique elements
arr=np.array(['Solid','Solid','Solid','Liquid','Liquid','Gas'])
print(np.unique(arr))

print("*"*50)

# Checking for the presdence of elements using in1d
print(np.in1d(['Solid','Liquid','Plasma'],arr))