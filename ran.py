import numpy as np

def ran(m,M,n):
	r0 = ((M[0]-m[0])*np.random.random(n)+m[0]).reshape(-1,1)
	r1 = ((M[1]-m[1])*np.random.random(n)+m[1]).reshape(-1,1)
	r = np.hstack((r0,r1))
	return r