from multiprocessing import Pool
import numpy as np
from ag import ag
from func_1 import funcObj_1

def funcObj_2(poblacion):
	i = 0
	respons = np.zeros(poblacion.shape[0])
	#hilos = Pool()
	while i < poblacion.shape[0]:
		hilos = Pool()
		param1 = [poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:],poblacion[i,:]]
		result = hilos.map(funcion,param1)
		hilos.close()
		hilos.join()
		result = np.array(result)
		respons[i] = result.mean()
		i = i+1
	return respons


def funcion(poblacion):
	y = ag(60,40,poblacion[0],poblacion[1],2,30,funcObj_1)
	y.run()
	return y.getValorMejorElemento()