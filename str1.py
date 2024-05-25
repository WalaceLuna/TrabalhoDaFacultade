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
def impr(codif):
    print (f'mensagem codificada--> {codif}')
    return 
a=le()
codif=codifica(a)
impr(codif)
