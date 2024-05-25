'''17. Uma certa firma fez uma pesquisa para saber se as pessoas gostaram ou não de um
novo produto lançado no mercado. Para isso, forneceu o sexo do entrevistado e sua
resposta (sim ou não). Sabendo-se que foram entrevistadas 2.000 pessoas, crie um
algoritmo que calcule e escreva:
a) o número de pessoas que responderam sim;
b) o número de pessoas que responderam não;a porcentagem de pessoas do
sexo masculino que responderam não.'''

#questao 17

quants=0
quantn=0
quant=0
m=0
for i in range(1,7):
    sexo=input('Digite o seu sexo (M/F): ')
    resposta=input('Digite se gostou do produto (S/N): ')
    print('='*20)
    if (resposta == 's') or (resposta == 'S'):
        quants+=1
    if (resposta == 'n') or (resposta == 'N'):
        quantn+=1
    if ((sexo == 'm') or (sexo == 'M')):
        m+=1
    if ((sexo == 'm') or (sexo == 'M')) and ((resposta == 'n') or (resposta == 'N')):
        quant+=1
porc=(quant*100)/m
print(f'{quants} pessoas que responderam "SIM"')
print(f'{quantn} pessoas que responderam "NÃO"')
print(f'a porcentagem de homens que responderam "NÃO" é de {porc}%')
