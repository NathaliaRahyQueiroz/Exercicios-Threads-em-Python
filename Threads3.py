import multiprocessing

import random



def processamento (sapo, distancia):
    total: int = 0
    pulo: int = 0
    
    while total < distancia:
        
        pulo = random.randint(1, 5)
            
        total = total + pulo
        
        if total >= distancia:
            print ('O sapo', sapo, 'chegou')
        else:
            print ('O sapo', sapo, 'deu um pulo de', pulo, 'cm e percorreu', total, 'cm')

    

def main():
    
    params = [(0, 0)] * 5
    distancia = int(input('Digite a distância total a ser percorrida:'))


    for i in range (5):
        
        params [i] = (i+1, distancia)
    
    with multiprocessing.Pool(processes=5) as pool:
        pool.starmap(processamento, params)

if __name__ == '__main__':
    main()