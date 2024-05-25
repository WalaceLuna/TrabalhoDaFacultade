'''5. Leia um vetor de 16 posições e troque as 8 primeiras posições pelas 8 últimas
posições. Imprima o vetor original e o vetor trocado.'''

vetor=[]

for i in range(1,9):
    vetor.append(int(input(f'Digite o {i} numero: ')))
primeiros=vetor[0:4]
ultimos=vetor[4:8]
print(primeiros)
print(ultimos)
vetor=ultimos + primeiros
print(vetor)
