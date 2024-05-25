'''3. Crie um algoritmo que leia uma quantidade não determinada de números inteiros. O
programa deve calcular e escrever a quantidade de números pares e ímpares e a
média aritmética dos números pares. A leitura deve ser encerrada quando for lido o
número zero, que não deve ser considerado.'''

#questao 3

somapar=0
quantpar=0
quantimpar=0
n=int(input('digite um numero: '))
print('='*20)
while(n!=0):
    if (n%2==0):
        somapar+=n
        quantpar+=1
    else:
        quantimpar+=1
    n=int(input('digite um numero: '))
    print('='*20)
mediapar=somapar/quantpar
print('existe', quantimpar,'numeros impares e', quantpar,'numeros pares')
print('a media dos numeros pares é', mediapar)
