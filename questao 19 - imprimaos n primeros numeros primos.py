'''19. Crie um algoritmo que leia um número N e imprima os N primeiros números
primos.'''

#questao 19


'''quant=0
cont=0
n=int(input('Digite a quantidade de numeros: '))
while (quant<n+1):
    for i in range(1,(n*2)+2):
        for j in range(1,i+1):
            if i%j==0:
                quant+=1
            cont+=1
            if cont == 2:
                print(i)'''

'''quant=0
cont=0
j=int(input('quantos numeros: '))
while(cont<j):
    n=int(input('asdas: '))
    for i in range(2,(n*2)+1):
        if n%i==0:
            quant+=1
            if quant == 1:
                print('primo')
                print(i)
                cont+=1
        quant=0'''


'''n=int(input('asdas: '))
if(n!= (2,3,5,7)):
    if n%2==0:
        p
    elif n%3==0:
        p
    elif n%5==0:
        p
    elif n%7==0:
        p'''

n=int(input('Digite um numero: '))
p=1
y=3
print('2')
while p<n:
    x=3
    while p<y:
        if y%x==0:
            break
        x+=2
    if x==y:
        print(x)
        p+=1
    y+=2


        

