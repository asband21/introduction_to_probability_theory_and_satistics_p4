import scipy as scp
import numpy as np
import matplotlib.pyplot as plt

X1 = scp.stats.norm(0,1) # Create object of a 'frozen' normal RV with mean = 0 and std = 1

print(dir(X1))

x = np.linspace(-20,20,1000)
pdf = X1.pdf(x)

plt.figure()
plt.plot(x,pdf)


X2 = scp.stats.norm(2,0.5) # Create object of a normal RV with mean = 1 and std = 0.5
a = 2 
b = 3

W = scp.stats.norm(a*X1.mean()+b*X2.mean(),a*X1.std()+b*X2.std())

pdfW = W.pdf(x)
plt.figure()
plt.plot(x,pdfW)
plt.show()
