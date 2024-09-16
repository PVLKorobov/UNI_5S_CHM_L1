import numpy as np
import matplotlib.pyplot as plt


n = int(input("Введите количество узлов n: ")) 
a = -1
b = 1

def f(x):
	


	return 1/(1+25*x*x)

def inter(n,a,b, x):
	z = np.linspace(a,b,n)
	s = 0

	for i in z:
		p1 = 1
		p2 = 1		
		for j in z:
			if i != j:
				p1 *= (x-j)
				p2 *= (i-j)
		s+=f(i) * (p1/p2)
	


	return s







#построение графика по средним точкам

print(np.linspace(a,b,n))
print(np.linspace(a,b,2*n-1))
len = abs(a)+abs(b)
k = n -1
print(len/k)

x = np.linspace(a,b,2*n-1)
y = f(x)


plt.plot(x,y)


x = np.linspace(a,b,2*n-1);
#x = np.linspace(a+len/(2*k),b-len/(2*k),n-1)
y = []
for d in x:
	y.append(inter(n,a,b,d))






plt.plot(x,y,'r')



plt.show()