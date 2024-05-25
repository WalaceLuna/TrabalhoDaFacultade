# gerar um numero inteiro aleatorio de 5 algarismos. P ex 00001

from random import *
def gera():
    num=''
    for i in range(5):
        ale=randint(0,9)
        alec=str(ale)
        num+=alec
    return num
def impr(num):
    print(f'O numero de 5 algarismos aleatorios gerado é {num}')
num=gera()
impr(num)
