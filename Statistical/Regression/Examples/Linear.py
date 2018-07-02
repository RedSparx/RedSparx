import matplotlib.pyplot as plt
import numpy as np

N=100
Std_Dev = 30;
Error = np.random.randn(N)*Std_Dev

m=10
b=4
x=np.linspace(-10,10,N)
y=m*x+b + Error
y_original=m*x+b

Sx = np.sum(x)
Sy = np.sum(y)
Sxx= np.sum(x*x)
Sxy= np.sum(x*y)

m_est = (N*Sxy-Sx*Sy)/(N*Sxx-Sx*Sx)
b_est = (Sxx*Sy-Sxy*Sx)/(N*Sxx-Sx*Sx)

print("Original Equation:  y = %2.1fx + %2.1f"%(m,b))
print("Estimated Equation: y = %2.1fx + %2.1f"%(m_est,b_est))

plt.plot(x,y,'*')
plt.plot(x,y_original)
plt.title("y = %2.1fx + %2.1f"%(m_est,b_est))
plt.show()