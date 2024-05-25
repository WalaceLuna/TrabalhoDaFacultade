'''14. Crie um algoritmo que:
a) Leia a idade de várias pessoas. O final da lista contém o valor da idade igual a
-1 que deverá ser computado.
b) Calcule e mostre a idade média desse grupo de indivíduos. Escreva também a
porcentagem de pessoas entre 21 e 65 anos inclusive.'''

#questao 14


quant=0
soma=0
quantp=0
idade=int(input('Digite a idade: '))
while(idade!=-1):
    quant+=1
    soma+=idade
    for i in range(21,66):
        if (idade == i):
            quantp+=1
    idade=int(input('Digite a idade: '))
media=soma/quant
porc=(quantp*100)/quant
print('='*15)
print(f'a media de idade das pessoas é de {media} anos')
print(f'a porcentagem de pessoas entre 21 e 65 anos é {porc}%')

