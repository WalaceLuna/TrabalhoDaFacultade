'''11. Crie um algoritmo que calcule a soma dos N primeiros números inteiros ímpares e
positivos. O valor de N deve ser lido do usuário.'''

#questao 11

soma=0
n=int(input('Digite um numero positivo: '))
for i in range(1,n+1):
    if(i%2!=0):
        soma+=i
print(f'a soma dos primeiros {n} primeiros numeros impares e positivos é {soma}')
