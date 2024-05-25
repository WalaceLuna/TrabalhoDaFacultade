'''4. Ler um vetor de números inteiros de 30 posições. Depois, ler um número inteiro X,
imprimir quantas vezes o número X aparece no vetor'''

lista=[]
quant=0

for i in range(1,5):
    lista.append(int(input(f'Digite o {i} numero: ')))
print('= ' * 10)
x=int(input('Digite um numero: '))
for j in range(0,4):
    if lista[j] == x:
        quant+=1
print(f'o numero {x} aparece {quant} vezes dentro da lista')
print(lista)

