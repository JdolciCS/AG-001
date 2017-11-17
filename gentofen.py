import numpy as np
def gentofen(n,largo,xmax,ymax,xmin,ymin):
	r = np.zeros((n.size,2))
	r[:,0] = (n/(2**32)).reshape(n.size,)
	r[:,1] = (n%(2**32)).reshape(n.size,)
	r = r / (10**(largo+1))
	r[:,0] = (r[:,0]*(xmax - xmin))+xmin#Normaliza los datos
	r[:,1] = (r[:,1]*(ymax - ymin))+ymin
	return r