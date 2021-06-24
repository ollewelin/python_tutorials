# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0, 10, 100)

# Plot the data
plt.plot(x, x, label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()

a = np.linspace(-5,5,1000)
def f(a): return a**(2)# 
print(f(4))
plt.plot(a, f(a))
plt.show()
print(a[700])
print(a[0])
print(a[999])
