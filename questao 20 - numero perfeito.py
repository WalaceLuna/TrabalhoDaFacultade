'''20. Crie um algoritmo que leia um número N e imprima se ele é perfeito ou não. Um
número é perfeito quando a soma dos seus divisores é igual a ele mesmo, e.g., 6 = 3 +
2 + 1.'''

#questao 20


soma=0
n=int(input('Digite um numero: '))
for i in range(1,n):
    if n%i==0:
        print(i)
        soma=soma+i
print('='*15)
if soma == n:
    print(f'{n} é um numero perfeito')
else:
    print(f'{n} Não é um numero perfeito')

