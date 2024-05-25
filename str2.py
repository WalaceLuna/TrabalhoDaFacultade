def le():
    a=input('Digite a mensagem-->  ')
    return a
def codifica(a):
    codif=''
    for i in range(0,len(a)): 
        letra=a[i] 
        cod=ord(letra) 
        cod1=chr(cod+1) 
        codif += cod1
    return codif
def decodifica(codif):
    dcodif=''
    for i in range(0,len(codif)): 
        letra=codif[i] 
        cod=ord(letra) 
        cod1=chr(cod-1)
        dcodif += cod1
    return dcodif
def impr(codif,decodif):
    print('\n**Criptografia**\n')
    print (f'mensagem codificada--> {codif}')
    print (f'mensagem decodificada--> {dcodif}')
    return 
a=le()
codif=codifica(a)
dcodif=decodifica(codif)
impr(codif,dcodif)
