'''6. Crie um algoritmo que leia a quantidade e o preço de 50 produtos comprados por
uma empresa. Ao final deve ser escrito o total gasto pela empresa.'''

#questao 6


soma=0
for i in range(1,3):
    quantidade=int(input(f'Digite a quantidade do produto numeor {i}: '))
    preco=float(input('qual o valor unitario desse produto: '))
    print('='*40)
    precoquant=preco*quantidade
    soma+=precoquant
print('='*40)
print(f'o total gasto pela empresa é no valor de R${soma}')
