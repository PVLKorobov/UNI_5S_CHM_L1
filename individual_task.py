import numpy as np
import math
import matplotlib.pyplot as plt
 
 
a = 0.5
b = 2
m = 10

for n in [10, 40, 60, 120, 200]:
	plt.ylim(0, 4)
	plt.xlim(0.5, 2.5)

	x = []
	y = []
	
	def f(x):
		return (1+x*x)/(1+abs(math.log(x)))
	
	def inter(n,a,b, x):
		z = np.linspace(a,b,n)
		s = 0
	
		for i in z:
			#print(f(i), i)
			p1 = 1
			p2 = 1		
			for j in z:
				if i != j:
					p1 *= (x-j)
					p2 *= (i-j)
			s+=f(i) * (p1/p2)
	
		return s
	
	x = np.linspace(a,b,3 + (n-1)*m)
	for xi in x:
		y.append(f(xi))
	
	
	
	plt.plot(x,y,label="Приближаемая функция")
	
	
	xl = []
	yl = 0
	#x = np.linspace(a+len/(2*k),b-len/(2*k),n-1)
	y = []
	for d in x:
		z = inter(n,a,b,d)
		if abs(f(d) - z) > 0.005:
	
			xl.append([abs(d), abs(f(d) - z)])
	
		y.append(z)
	
	
	
	xl.append([b, 10000])
	
	
	plt.plot(x,y,'r',label="Интерполяция в узлах и дополнительных точках")
	# plt.axvline(x = min(xl, key=lambda i: i[1] if i[0] < 1.5 else 1000 )[0], linewidth=4, color='g')
	# plt.axvline(x = min(xl, key=lambda i: i[1] if i[0] > 1.5 else 1000 )[0], linewidth=4, color='g')

	intervalLeft = round(min(xl, key=lambda i: i[1] if i[0] < 1.5 else 1000 )[0], 2)
	intervalRight = round(min(xl, key=lambda i: i[1] if i[0] > 1.5 else 1000 )[0], 2)
	
	plt.figtext(0,0,f"Интервал сходимости: [{intervalLeft}, {intervalRight}]")
	plt.title(f"n={n}")
	plt.legend(loc="upper right")
	plt.savefig(f"graph_png/{n}.png")
	plt.clf()