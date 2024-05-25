'''2. Leia um vetor de 40 posições e conte quantos elementos pares se encontram no
vetor.'''


vetor=[]
resultado=[]
quant=0

for i in range(1,5):
    vetor.append(int(input(f'Digite o valor do {i} numero: ')))
for j in range(0,4):
    if vetor[j]%2==0:
        resultado.append(vetor[j])
        quant+=1
print(f'existem {quant} numeros pares')
print(resultado)
