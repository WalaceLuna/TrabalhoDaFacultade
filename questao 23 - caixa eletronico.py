'''23. Crie um algoritmo de caixa eletrônico que lê a quantidade de dinheiro a ser sacado
e imprime a menor quantidade de notas a ser dada ao usuário. Assume-se que existam
notas de 50, 20, 10, 5 e 1. Imprimir também a quantidade de cada nota a ser dada ao
usuário. O final da leitura é marcado pelo valor 0 que não deve ser calculado.
Exemplo: 98 = uma nota de 50, duas notas de 20, uma nota de 5, e três notas de 1.'''

#questao 23




din=1

while din != 0:

    
    soma=0
    soma50=0
    soma20=0
    soma10=0
    soma5=0
    soma1=0

    
    din=float(input('Digite o valor que deseja sacar: R$'))
    dinf=din
    if din == 0:
        break




    while din>0:
        if din>=50:
            soma50+=1
            soma+=50
            din-=50
        elif din>=20:
            soma20+=1
            soma+=20
            din-=20
        elif din>=10:
            soma10+=1
            soma+=10
            din-=10
        elif din>=5:
            soma5+=1
            soma+=5
            din-=5
        else:
            soma1+=int(din)
            soma+=din
            din-=din



    din=dinf



    print()        
    print(f'R${dinf} = {soma50} nota de R$50, {soma20} notas de R$20, {soma10} nota de R$10, {soma5} nota de R$5, e {soma1} notas de R$1')
    print()  
    print('= '*40)
    print()
