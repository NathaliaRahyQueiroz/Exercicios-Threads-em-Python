import multiprocessing
import time
import random

def processamento(id, vl):
    soma = 0 
    for valor in (vl):
        soma = soma + valor
        time.sleep(0.2)

    print ('A linha', id, 'tem soma =', soma)
    

def main():
    i: int = 0
    id: int = 0
    
    params: int = [(0, 0)]*3
    
    
    for i in range (3):
        valores: int = [0]*5
        id = int(input("Digite o id:"))
        for v in range (0, 5, 1):
            valores[v] = random.randint(1, 100)
        params[i] = (id, valores)
        print (params)
        
    with multiprocessing.Pool(processes=3) as pool:
        pool.starmap(processamento, params) 
        
    

      

if __name__ == '__main__':
    main()