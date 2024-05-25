'''4. Crie um algoritmo que leia os nomes e os preços dos produtos de uma loja e que
escreva o nome do produto mais caro. Considere que o final da lista é marcado pelo
produto ‘XXX’ e que não existem preços repetidos.'''

#questao 4

caro=0
nome=input('Digite o nome do produto: ')
while(nome!='xxx')and (nome!='XXX'):
    preco=float(input('Digite o preço do produto: '))
    if(preco>caro):
        caro=preco
        nomecaro=nome
    print('='*30)
    nome=input('Digite o nome do produto: ')
print('='*35)
print('o produto mais caro é', nomecaro)


    
