'''21. Crie um algoritmo que imprima os 4 primeiros números perfeitos.'''

cont = 0
n = 1
while(cont != 4):
    n+=1
    soma= 0
    for i in range(1,n):
        if(n%i==0):
            soma+=i
    if(soma==n):
        print(n)
        cont+=1
