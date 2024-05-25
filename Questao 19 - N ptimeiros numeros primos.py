'''19. Crie um algoritmo que leia um número N e imprima os N primeiros números
primos. O seu programa deve fazer o MÍNIMO de interações possíveis.'''

n=int(input('Insira um numero N para ver os N primeiros números primos: '))
cont=0
i=2
while(cont != n):
    div=0
    for j in range(1, i+1):
        if(i%j == 0):
            div += 1
    if(div == 2):
        print(i)
        cont += 1
    i += 1
    
