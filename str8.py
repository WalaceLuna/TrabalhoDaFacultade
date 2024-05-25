'''Crie programa que receba duas palavras, retorne exiba ‘E prefixo’ ou ‘Não é prefixo’
 caso a primeira palavra seja um prefixo da segunda. 
Exemplo: ’ue’ é prefixo de ’uerj’. ’uerj’ não é prefixo de ’ue’.'''
def le():
    palav1=input('Digite a primeira palavra ').strip()
    palav2=input('Digite a segunda palavra ').strip()
    return palav1,palav2
def compa(palav1,palav2):
    # converte em maiusculas mas não altera as frases lidas
    palav1=palav1.upper()
    palav2=palav2.upper()
    prefix=False
    if len(palav1)>len(palav2):
        return prefix
    i = 0
    while i<len(palav1):
        if palav1[i]!=palav2[i]:
            return prefix
        i = i+1
    prefix=True
    return prefix
def impr(prefix,palav1,palav2):
    if prefix:
        print(f'A palavra {palav1} é prefixo de {palav2}')
    else:    
        print(f'A palavra {palav1} não é prefixo de {palav2}')
    return
palav1,palav2=le()
prefix=compa(palav1,palav2)
impr(prefix,palav1,palav2)
