import numpy as np
import matplotlib.pyplot as plt

# Ploting Numpy Arrays using matplotlib

# Use numpy meshgrid
axes_values=np.arange(-100,100,10)

dx,dy=np.meshgrid(axes_values,axes_values)
print(dx)
print(dy)

print("*"*50)

# Plot the function
function=2*dx+3*dy
print(function)

print("*"*50)

plt.imshow(function)
plt.title("Function of 2*x + 3*dy")
plt.colorbar()
plt.savefig('myfig.png')

function2=np.cos(dx)+np.cos(dy)
print(function2)

print("*"*50)

plt.imshow(function2)
plt.title("Function of cos plot")
plt.colorbar()
plt.savefig('myfig2.png')
