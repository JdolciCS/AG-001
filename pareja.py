import numpy as np

def pareja(n,rank,mut,cross):
	hijo = np.zeros((rank.size))
	hijo[0] = n[np.argmax(rank)]
	i=1
	while i<(rank.size//2):
		#Ruleta al padre
		aux = np.random.rand()*(np.sum(rank))
		padre = -1
		while aux>0:
			padre += 1
			aux = aux - rank[padre]
		#Ruleta a la madre
		aux = np.random.rand()*(np.sum(rank))
		madre = -1
		while aux>0:
			madre += 1
			aux = aux - rank[madre]
		#Creo los hijos
		hijo[(i*2)-1] = n[padre]
		hijo[(i*2)] = n[madre]
		#Probabilidad de cruzamiento
		c = np.random.rand()
		if c<cross:
			cp = (2**(np.random.randint(63)))-1 #000011111
			hijo[(i*2)-1] = (n[padre]&~cp)|(n[madre]&cp)
			hijo[(i*2)] = (n[madre]&~cp)|(n[padre]&cp)
		#Probabilidad de mutamiento
		m = np.random.rand()
		if m<mut:
			mp = 2**(np.random.randint(63))
			if np.random.randint(2):
				hijo[(i*2)-1] = int(hijo[i*2]-1)^mp
			else:
				hijo[(i*2)] = int(hijo[(i*2)])^mp
		i = i+1
	return hijo