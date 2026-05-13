import platform
import subprocess
import multiprocessing


def f_so():
    system: str = ''
    system = platform.system()
    
    return system

def processamento(processo, servidor):
    saida: str = ''
    linha: str = ''
    vet_linha: str = []
    vet_proc: str = []
    vet_proc = processo.split()

    

    saida = subprocess.Popen(vet_proc, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')

    while linha != '':
       
        
        if 'tempo' in linha:
            vet_linha = linha.split()
            
            print (servidor, vet_linha[4])

        if 'time=' in linha:
            vet_linha = linha.split() 
            print (servidor, vet_linha[7] + vet_linha[8])
        
        if 'Mdia' in linha:
            vet_linha = linha.split()
            print (servidor, vet_linha[6] + vet_linha[7] + vet_linha[8])

        if 'avg' in linha:
            vet_linha = linha.split()
            
            vet_avg = vet_linha[1].split('/')
            vet_num = vet_linha[3]. split('/')
            print(servidor, vet_avg[1] +  vet_linha[2] +  vet_num[1] +  vet_linha[4])
        
        linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')


def main():
    params: str = [0] * 3
    serv: str = ['www.uol.com.br', 'www.terra.com.br', 'www.google.com.br']
    servidor: str = ['UOL', 'Terra', 'Google']
    sistema: str = ''
    sistema = f_so()

    for i in range (3):
        if sistema == 'Windows':

            params [i] = ('ping -4 -n 10 ' + serv[i], servidor[i])

        elif sistema ==  'Linux':

            params [i] = ('ping -4 -c 10 '+ serv[i], servidor[i])

        
    with multiprocessing.Pool(processes=3) as pool:
        pool.starmap(processamento, params)

if __name__ == '__main__':
    main()