'''Elabore um programa que leia uma frase (sem espaços em branco),
determine o número de segmentos consecutivos que compõem a frase.
Exemplo:
’AAAAAbbbbbcccccccCCCDDDDDddd’ contém 6 segmentos.
’AAAAA’ contém 1 segmento.'''
def le():
    frase=input('Digite a frase ')
    return frase
def segmentos_consecutivos(frase):
    elemento  =  frase[0]
    contador = 1
    for k in frase:
        if  elemento!=k:
            contador = contador+1
            elemento = k
    return   contador
def impr(contador):
    print(f'A frase tem {contador} segmentos consecutivos')
    return
frase=le()
contador=segmentos_consecutivos(frase)
impr(contador)
