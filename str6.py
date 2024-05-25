# gerar "n"  palavras aleatórias de 5  a 10 letras
# o codigo ascii para as letras varia de codigo 97 letra a até 122 letra z
from random import * # importa a biblioteca
def gera():
    palav='' # cria uma palavra vazia
    n=randint(5,10)
    for i in range(n):
        letra=chr(randint(97,122)) # gera letra aleatoria
        palav+=letra # incorpora a letra gerada a palavra
    return palav
def impr(palav):
    print(f'palavra aleatória {palav}')
    return
n=int(input('Digite a quantidade de palavras a serem geradas '))
for i in range(n):
    palav=gera()
    impr(palav)
