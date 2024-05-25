'''8. Considere um vetor de trajetórias de 9 elementos onde cada elemento possui o
valor do próximo elemento a ser lido.

Índice 0 1 2 3 4 5 6 7 8
Valor  4 6 5 8 1 7 3 0 2

Fazer um programa que leia esse vetor e imprima a trajetória correta: sequência de
impressão 4, 1, 6, 3, 8, 2, 5, 7, 0.'''

def ler (vetor):
    x = 0
    s = []
    for i in range(0,len(vetor)):
        s.append(vetor[x])
        x = vetor[x]
    return s

def imprime(x,y):
    for i in range(0,len(x)):
        print(i, end = ' ')
    print()
    for j in range(0,len(y)):
        print(y[j], end = ' ')
    print()
    
vetor1=[4,6,5,8,1,7,3,0,2]
vetor2= ler(vetor1)
imprime(vetor1,vetor2)


