'''16. Crie um algoritmo que:
a) Leia e escreva o nome e a altura das moças inscritas em um concurso de
beleza, até que seja digitada o nome ‘MARIA’, que marca o final da lista, mas é
para ser computada no concurso.
b) Calcule e escreva as duas maiores alturas e quantas moças as possuem.'''

#questao 16

maria=0
maisalto=0
segundomaisalto=0
quantmais=1
quant2mais=1
while(maria!=1):
    nome=input('Digite o nome: ')
    altura=float(input('Digite a altura: '))
    print('='*20)
    if nome == 'maria':
        maria=1
    if altura == maisalto:
        quantmais+=1
    if altura == segundomaisalto:
        quant2mais+=1
    if altura > maisalto:
        segundomaisalto=maisalto
        maisalto=altura
        quantmais=1
    elif (altura < maisalto)and(altura > segundomaisalto):
        segundomaisalto=altura
        quant2mais=1

print(f'a moça mais alta tem {maisalto} e {quantmais} pessoas tem essa altura')
print(f'a segunda moça mais alta tem {segundomaisalto} e {quant2mais} pessoas tem essa altura')
        
        
