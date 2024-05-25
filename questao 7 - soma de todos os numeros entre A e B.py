'''7. Crie um algoritmo que leia 2 números inteiros positivos, A e B, e que calcule a soma
de todos os números compreendidos entre eles. Os valores A e B não devem ser
considerados no somatório. Caso A seja maior do que B deve ser enviada uma
mensagem para o usuário informando que a soma não será realizada.'''

#questao 7

soma=0
a=int(input('Digite o primeiro numero: '))
b=int(input('Digite o segundo numero: '))
if(a>b):
    print('*** ERRO!!! *** A SOMA NÃO SERÁ REALIZADA!!!')
else:
    for i in range(a+1,b):
        soma+=i
print('='*25)
print(f'a soma de todos os numeros entre {a} e {b} é {soma} ')    
