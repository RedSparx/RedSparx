import numpy as np
import matplotlib.pyplot as plt

#region Notes
# This program will estimate coefficients for the following model: y = alpha*exp(beta*x).  In order to do this, the
# model will be transformed so that it looks like the following:
#
#                                   ln(y) = ln(alpha) + beta*x
#
# This transformation allows for linear regression to be used.  Note that the transformation function may cause
# problems.  If any data point is negative, the logarithm is not defined.  This is important when impaired (noisy) data
# may sometimes be negative (the model may positive definite, but errors are additive and can be both positive and
# negative).  This is a drawback for this method, but can be overcome for the sake of obtaining an estimate.
#endregion

#region Generate exponential data.
N = 50
x_start=0.0
x_end=15.0
x=np.linspace(x_start, x_end, N)
alpha = 10.0
beta = -0.1
y=alpha*np.exp(beta*x)
Sigma=0.75
Error=np.random.randn(N)*Sigma
y_experimental=y+Error
#endregion

#region Generate statistics.
Sxy=np.sum(x*np.log(y_experimental))
Sxx=np.sum(x*x)
Sx=np.sum(x)
Sy=np.sum(np.log(y_experimental))

N=np.float(N)
beta_est = (N*Sxy-Sx*Sy)/(N*Sxx-Sx*Sx)
ln_alpha_est = (Sxx*Sy-Sxy*Sx)/(N*Sxx-Sx*Sx)
alpha_est = np.exp(ln_alpha_est)
#endregion

#region Generate estimated model.
y_model=alpha_est*np.exp(beta_est*x)
print(alpha_est)
print(beta_est)
#endregion

#region Plot results.
plt.plot(x,y_experimental,'y*')
plt.plot(x,y_model,'b')
plt.plot(x,y,'r--')

plt.text(8,8,'$y=%2.1fe^{%2.1fx}$'%(alpha_est,beta_est))
plt.show()
#endregion