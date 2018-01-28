import numpy as np


def funcObj_1(poblacion):
		##aux = poblacion[:,0]**2 + poblacion[:,1]**2
		##r = np.sqrt(aux)
		##s_2 = (np.sin(r)**2)-0.5
		##d = (1 + (0.001*(aux)))**2
		##r = 0.5 - (s_2/d)
		##f = r
		X = poblacion[:,0]
		Y = poblacion[:,1]
		a = 20
		b = 0.2
		c = 2*3.1415926535
		r1 = -a * np.exp( -b * np.sqrt( ((X**2) + (Y**2))/2 ) )
		r2 = -1 * np.exp( (np.cos(c * X)+np.cos(c * Y))/2 )
		r3 = np.exp(1)
		f = (r1+r2+a+r3)
		return f