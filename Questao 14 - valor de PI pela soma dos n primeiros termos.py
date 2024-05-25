'''14. Faça um programa que calcule o valor de PI pela soma dos n primeiros termos da
série abaixo:'''

import math
soma=0
n=int(input('Insira um numero n para calcular o valor de PI pela soma dos n primeiros numeros da serie: '))

for i inh range(1, n+1):
    if(i%2==1):
        soma+=1/(i**2)
    else:
        soma+=(1/(i**2))*-1
print(math.sqrt(12*(soma)))
