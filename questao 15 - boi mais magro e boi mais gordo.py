'''15. Num frigorífico existem 90 bois. Cada boi traz preso em seu pescoço um cartão
contendo seu número de identificação e seu peso. Crie um algoritmo que escreva o
número e peso do boi mais gordo e do boi mais magro.
Além disso, responda: se houver dois ou mais bois com o mesmo peso, maior que
todos os demais, este algoritmo escreverá o número de qual deles?'''

#questao 15

nomegordo=0
nomemagro=0
magro=0
gordo=0
pesoigual=[]
for i in range(1,5):
    iden=input('Digite a identificação que consta no pescoço: ')
    peso=int(input('Digite o peso do boi: '))
    print('='*50)
    if (peso == gordo):
        pesoigual= nomegordo + ', ' + iden
        nomegordo=pesoigual
    if (peso > gordo):
        gordo=peso
        nomegordo=iden
    elif(magro == 0):
            magro=peso
    if (peso < magro):
        magro=peso
        nomemagro=iden
print(f'o boi mais gordo é o {nomegordo} que tem {gordo}kg e o boi mais magro é o {nomemagro} que tem {magro}kg')
