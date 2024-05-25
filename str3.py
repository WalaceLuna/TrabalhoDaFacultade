# str3 Conte a quantidade de espaços em branco de uma string
def le():
    frase=input('Digite uma frase ')
    return frase
def conta1(frase):
    # solução 1
    tam=len(frase)
    cont1=0
    for i in range(tam):
        if frase[i]==' ':
            cont1+=1
    return cont1
def conta2(frase):
    cont2=0
    for i in frase:
        if i==' ':
            cont2+=1
    return cont2
def conta3(frase):
    cont3=frase.count(' ')
    return cont3
def impr(frase,cont1,cont2,cont3):
    print(f'A frase {frase} contem {cont1} espaços em branco - metodo 1')
    print(f'A frase {frase} contem {cont2} espaços em branco - metodo 2')
    print(f'A frase {frase} contem {cont3} espaços em branco - metodo 3')
    
frase=le()
cont1=conta1(frase)
cont2=conta2(frase)
cont3=conta3(frase)
impr(frase,cont1,cont2,cont3)

