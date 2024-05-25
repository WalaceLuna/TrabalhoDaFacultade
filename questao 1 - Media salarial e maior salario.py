'''1. A prefeitura de uma cidade resolveu fazer uma pesquisa entre os seus
trabalhadores. Para isso ela coletou alguns dados como idade, sexo (M ou F) e salário.
Crie um algoritmo que leia estes dados e que escreva ao final:
a) a média salarial dos homens, a média salarial das mulheres
b) o maior salário encontrado entre as pessoas abaixo de 30 anos.
Obs: O final da leitura de dados é marcado por uma idade negativa.
'''

#quetao 1

quantf=0
quantm=0
somam=0
somaf=0
maiorsalario=0

idade=int(input('digite a idade: '))
while(idade>=0):
    sexo=input('digite o sexo (F/M): ')
    salario=float(input('Digite o salario: '))
    print('='*25)
    if(sexo == 'm')or (sexo == 'M'):
        quantm+=1
        somam+=salario
    if(sexo == 'f')or (sexo == 'F'):
        quantf+=1
        somaf+=salario
    if(idade<30):
        if(salario>maiorsalario):
            maiorsalario=salario
    idade=int(input('digite a idade: '))
mediam=somam/quantm
mediaf=somaf/quantf
print('='*30)
print('a media salarial dos homens é', mediam, 'e a media salarial das mulheres é', mediaf)
print('o maior salario das pessoas abaixo de 30 anos é', maiorsalario)
    
