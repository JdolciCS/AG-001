###librerias###
import numpy as np
###Esta es la funcion a maximizar
# out = 1-(0.5 - (s_2./((1.+(0.001.*(x.^2.+y.^2))).^2)))
def fun(X,Y):
	r = np.sqrt(X**2 + Y**2)
	s_2 = (np.sin(r)**2)-0.5
	d = (1 + (0.001*(X**2 + Y**2)))**2
	r = 0.5 - (s_2/d)
	r = r
	return r