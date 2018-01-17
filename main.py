from multiprocessing import Pool
from ag import ag

def f(nG=10,nI=20,pM=0.8,pC=0.8,nGs=2,dF=30):
	x = ag(nG,nI,pM,pC,nGs,dF)
	x.run()
	return x	

if __name__ == '__main__':
	hilos = Pool(1)
	param1 = [100]
	param2 = [20,20]
	result = hilos.map(f,param1)
	hilos.close()
	hilos.join()
	print(result[0].getMejorElemento())
	print(result[0].getValorMejorElemento())