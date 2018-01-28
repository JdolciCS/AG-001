from multiprocessing import Pool
from ag import ag
from func_2 import funcObj_2




	
def f(nG=60,nI=40,pM=0.1,pC=0.8,nGs=2,dF=1,func=funcObj_2):
	x = ag(nG,nI,pM,pC,nGs,dF,func)
	x.run()
	return x	

if __name__ == '__main__':
	hilos = Pool()
	result = f()
	print(result.getMejorElemento())
	print(result.getValorMejorElemento())
	result.curvas()
	'''hilos = Pool()
	param1 = [50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]
	param2 = [20,20]
	result = hilos.map(f,param1)
	hilos.close()
	hilos.join()
	print(result[0].getMejorElemento())
	print(result[0].getValorMejorElemento())
	print(result[1].getMejorElemento())
	print(result[1].getValorMejorElemento())
	print(result[2].getMejorElemento())
	print(result[2].getValorMejorElemento())
	print(result[3].getMejorElemento())
	print(result[3].getValorMejorElemento())'''