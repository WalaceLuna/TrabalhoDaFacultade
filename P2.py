def   sufixo(palavra1,   palavra2):
    n1 = len(palavra1)
    n2 = len(palavra2)
    if n1 > n2:
        return  False
    j = 0
    while j<n1:
        if palavra1[n1-1-j] != palavra2[n2-1-j]:
            return False
        j= j+1
    return True
def impr(palavra1,palavra2):
    if sufixo(palavra1,palavra2):
        print(f'{palavra1} é sufixo de {palavra2}')
    else:    
        print(f'{palavra1} não é sufixo de {palavra2}')
    return
def le():
    palavra1=input('Digite a primeira palavra ')
    palavra2=input('Digite a segunda palavra ')
    return palavra1,palavra2
# programa principal
while True:
    try:
        n=int(input('Digite a quantidade de pares de palavras '))
        if n==0:raise
        break
    except:
        print('**erro** Quantidade errada - digite novamente')

for i in range(n):
    palavra1,palavra2=le()
    impr(palavra1,palavra2)

