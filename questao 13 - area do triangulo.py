'''13. Crie um algoritmo para calcular a área de um triângulo qualquer, considerando que
são fornecidos os comprimentos dos seus lados. Esse programa não pode permitir a
entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.'''

#questao 13

h=int(input('Digite a altura: '))
b=int(input('Digite o valor da base: '))
if(h or b)<=0:
    print('*** ERRO!!! ***')
else:
    area=(b*h)/2
print(f'a area do triangulo é {area}')
    
    
