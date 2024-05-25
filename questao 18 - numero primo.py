'''18. Crie um algoritmo que leia um número N e verifique se ele é primo.'''

#questao 18

quant=0
n=int(input('Digite um numero: '))
print()
for i in range(1,n+1):
    if n%i == 0:
        quant+=1
        print(f'{n} é divisivel por {i}')
print()
if quant > 2:
    print(f'*** {n} não é um numero primo ***')
else:
    print(f'*** {n} é um numero primo ***')
    
