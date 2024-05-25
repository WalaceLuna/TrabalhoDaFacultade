'''5. Crie um algoritmo que imprima o peso total que será carregado por um caminhão.
Sabe-se que este caminhão carrega 25 caixas. O peso de cada caixa deve ser informado
pelo usuário.'''

#questao 5


soma=0
for i in range(1,26):
    peso=int(input(f'qual o peso da caixa numero {i}: '))
    soma+=peso
    print('='*35)
print(f'o peso total da carga que o caminha levara é de {soma}')
