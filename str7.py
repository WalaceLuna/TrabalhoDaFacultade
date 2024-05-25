def ler ():
    s1=input('Digite a primeira frase ')
    s2=input('Digite a segunda frase ')
    return s1,s2

def compara_comprimento (s1,s2):
    tam_s1=len(s1)
    tam_s2=len(s2)
    print('Frases lidas: ',end=' ')
    print(f'{s1} -  tem tamanho {tam_s1} caracteres e ',end=' ')
    print(f'{s2} - tem tamanho {tam_s2} caracteres')
    print(f'Conclusão:\nAs frases:', end='')
    if tam_s1 == tam_s2:
        print('possuem o mesmo tamanho e',end=' ')
    else:
        print('não possuem o mesmo tamanho',end=' ')
    if s1==s2:
        print('e possuem o mesmo conteudo')
    else:
        print('e não possuem o mesmo conteudo')
    return

#main
x,y=ler()
compara_comprimento(x,y)
