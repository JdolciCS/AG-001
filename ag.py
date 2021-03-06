import matplotlib.pyplot as plt
import numpy as np

class ag():
	''' Propiedades estaticas'''
	''' Metodos '''
	def __init__(self,nG=20,nI=20,pM=0.1,pC=0.8,nGs=2,dF=10,func = 0):
		self.numGeneraciones = nG
		self.numIndividuos   = nI
		self.probMut         = pM
		self.probCross       = pC
		self.numGenes        = nGs
		self.domFunc         = dF
		self.prec            = 8
		self.funcObj_p       = func
		self.mejorElemento   = 0
		self.valorMejorElemento = 0;
		''' Variables para los graficos '''
		self.mejoresElementos = np.zeros((nG))
		self.off_line         = np.zeros((nG))
		self.on_line          = np.zeros((nG))
		self.sum_offLine      = 0
		self.sum_onLine       = 0
		self.axesX            = np.arange(1,nG+1,1)
	
	def curvas(self):
		plt.figure(3)
		plt.subplot(2,2,2)
		plt.plot(self.axesX,self.mejoresElementos,'-')
		plt.title('Mejores elementos')
		plt.subplot(2,2,3)
		p = plt.plot(self.axesX,self.off_line,'--',label = "Off-line")
		plt.title('off-line')
		plt.subplot(2,2,4)
		plt.plot(self.axesX,self.on_line,'-.',label = "on-line")
		plt.title('on-line')
		plt.show()

	def getMejorElemento(self):
		return self.mejorElemento

	def getValorMejorElemento(self):
		return self.valorMejorElemento

	def run(self):
		poblacion = self.rand()
		result = self.funcObj_p(poblacion)
		fitness = 1/(result)
		iter = 0
		while iter < self.numGeneraciones:
			poblacion = self.operadores(poblacion,fitness)
			result = self.funcObj_p(poblacion)
			fitness = 1/(result)
			''' Datos de los graficos '''
			self.mejoresElementos[iter] = np.amax(fitness)
			self.sum_offLine            = self.sum_offLine + np.amin(result)
			self.sum_onLine             = self.sum_onLine  + np.mean(result)
			self.off_line[iter]         = self.sum_offLine/(iter+1)
			self.on_line[iter]          = self.sum_onLine/(iter+1)
			iter = iter + 1 
		self.mejorElemento = poblacion[np.argmax(fitness),:]
		self.valorMejorElemento = np.amin(result)

	def rand(self):
		result = (((2*self.domFunc)*np.random.rand(self.numIndividuos,self.numGenes))-self.domFunc)#.reshape(-1,2)
		#i = 1
		#while i<self.numGenes:
		#	aux = ((2*self.domFunc)*np.random.rand(self.numIndividuos)-self.domFunc).reshape(-1,1)
		#	result = np.hstack((result,aux))
		#	i = i+1
		return result 

	def funcObj(self,poblacion):
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

	def operadores(self,poblacion,fitness):
		poblacion = (poblacion + self.domFunc) / (2 * self.domFunc)
		poblacion = poblacion * (10**(self.prec + 1))
		poblacion = poblacion.astype(int)
		hijos = np.zeros(poblacion.shape)
		#hijos[0,:] = poblacion[np.argmax(fitness),:]
		i = 0
		l = fitness.size//2
		while i<l:
			#Ruleta para elegir al padre
			aux = np.random.rand()*(np.sum(fitness))
			iPadre = -1
			while aux>0:
				iPadre += 1
				aux = aux - fitness[iPadre]
			#Ruleta para elegir a la madre
			aux = np.random.rand()*(np.sum(fitness))
			iMadre = -1
			while aux>0:
				iMadre  += 1
				aux = aux - fitness[iMadre]
			hijos[(i*2),:]   = poblacion[iPadre,:]
			hijos[(i*2)+1,:] = poblacion[iMadre,:]
			pCross = np.random.rand()
			if pCross < self.probCross:
				posicionCross = np.random.randint(self.numGenes * 32)
				iVar = 0
				lMed = (posicionCross+1)//32
				lVar = self.numGenes
				while iVar < lMed:
					hijos[(i*2),iVar]   = poblacion[iPadre,iVar]
					hijos[(i*2)+1,iVar] = poblacion[iMadre,iVar]
					iVar += 1
				mod = ( (posicionCross+1) % 32 )
				if mod!=0 :
					mascBits = (2**(32-mod))-1 #000111
					hijos[(i*2),iVar]   = (poblacion[iPadre,iVar]&~mascBits)|(poblacion[iMadre,iVar]&mascBits)
					hijos[(i*2)+1,iVar] = (poblacion[iMadre,iVar]&~mascBits)|(poblacion[iPadre,iVar]&mascBits)
					iVar += 1
				while iVar < lVar:
					hijos[(i*2),iVar]   = poblacion[iMadre,iVar]
					hijos[(i*2)+1,iVar] = poblacion[iPadre,iVar]
					iVar += 1
			pMut = np.random.rand()
			if pMut < self.probMut :
				posicionMut = np.random.randint(self.numGenes * 32)
				iVar = posicionMut//32
				mod  = posicionMut%32
				mascBits = (2**(32-mod-1))#000100
				if np.random.randint(2) :
					hijos[(i*2),iVar] = int(hijos[(i*2),iVar])^mascBits
				else:
					hijos[(i*2)+1,iVar] = int(hijos[(i*2)+1,iVar])^mascBits
			i += 1
		hijos[0,:] = poblacion[np.argmax(fitness),:]
		hijos = hijos / (10**(self.prec + 1))
		hijos = (hijos * (2 * self.domFunc)) - self.domFunc
		return hijos