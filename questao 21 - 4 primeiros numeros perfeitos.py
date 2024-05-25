'''21. Crie um algoritmo que imprima os 4 primeiros números perfeitos.'''

#questao 21

''''cont=0
n=0
print('Os 4 primeiros numeros perfeitos são:')
print('= '*20)
while cont <4:
    n+=1
    soma=0
    for j in range(1,n):
        if n%j==0:
            soma+=j
    if soma == n:
        print(soma)
        print('='*6)
        cont+=1'''
    
    



#outra forma de resolver            
                
#21. Crie um algoritmo que imprima os k primeiros números perfeitos.

cont=0
n=0
k=int(input('Digite um numero: '))
print()
print('= '*20)
print(f'Os {k} primeiros numeros perfeitos são:')
print('= '*20)
print()
while cont <k:
    n+=1
    soma=0
    for j in range(1,n):
        if n%j==0:
            soma+=j
    if soma == n:
        print(soma)
        print('='*6)
        cont+=1

