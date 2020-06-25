import matplotlib.pyplot as plt
import numpy as np

def xn1(xn, r):
	return r*xn*(1-xn)

def finalvalues(r):
	x0 = 0.4

	values = []

	xn = x0
	for i in range(1,1000):
		result = xn1(xn, r)
		values.append(result)
		xn = result

	return values[-100:]


xvalues = []
yvalues = []
for r in np.arange(2.8,5,0.0001):
	yvalues.extend(finalvalues(r))
	xvalues.extend([r]*100)

plt.plot(xvalues, yvalues, '.', markersize=0.05)
plt.show()