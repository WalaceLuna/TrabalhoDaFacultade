'''12. Crie um algoritmo que calcule a soma dos primeiros 50 números pares. Os
primeiros números pares são: 2, 4, 6, ...'''

#questao 12

soma=0
for i in range(2,51*2,2):
    soma+=i
print(f'a soma dos 50 primeiros numeros pares é {soma}')
