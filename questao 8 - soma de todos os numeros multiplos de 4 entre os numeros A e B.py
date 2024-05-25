'''8. Crie um algoritmo que leia 2 números inteiros positivos, A e B, e que calcule a soma
de todos os números múltiplos de 4 compreendidos entre eles. Os valores A e B não
devem ser considerados no somatório. Caso A seja maior do que B deve ser enviada
uma mensagem para o usuário informando que a soma não será realizada.'''

#questao 8


soma=0
a=int(input('Digite o primeiro numero: '))
b=int(input('Digite o segundo numero: '))
if(a>b):
    print('*** ERRO!!!***')
else:
    for i in range(a+1,b):
        if(i%4==0):
            soma+=i
if(a<b):
    print('='*30)
    print(f'a soma dos numeros multiplos de 4 entre os numeros {a} e {b} é {soma}')
