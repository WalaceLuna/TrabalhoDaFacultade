# ler uma frase e verificar se é palindroma
def le():
    frase=input('Digite a frase ').strip()
    return frase
def metodo1(frase):
    # retirar espaços em branco da frase
    frasesem=frase.replace(' ','')
    # inverter a frase
    inv=frasesem[::-1]
    return inv,frasesem
    
def metodo2(frase):
    
    frasesem=inv=''
    tam=len(frase)
    # retirar espaços em branco 
    for i in range(tam):
        if frase[i]!=' ':
            frasesem+=frase[i]
    tam1=len(frasesem)
     # inverter sem espaços em branco
    for i in range(-1,-(tam1+1),-1):
         inv+=frasesem[i]
    return    inv,frasesem
        
def impr(metodo,frase,frasesem,inv):
    print(f'Usando o metodo {metodo}')
    print(f'A frase {frase} ',end=' ')
    if frasesem==inv:
        print(f'é palidroma')
    else:
        print(f'não é palíndroma')
    return
frase=le()
inv,frasesem=metodo1(frase)
impr('metodo 1 ',frase,frasesem,inv)
inv,frasesem=metodo2(frase)
impr('metodo 2 ',frase,frasesem,inv)
