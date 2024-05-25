# walace nunes luna
# segunda prova - P2
def le():
    # colocando strip no final para excluir qualquer espaço vazio no inicio e no final da palavra
    primeira=input('Digite a primeira palavra ').strip()
    segunda=input('Digite a segunda palavra ').strip()
    return primeira,segunda
def comparacao(primeira,segunda):
    # upper para converte em maiusculas todas as letras para não ocorre erros
    primeira = primeira.upper()
    primeira = segunda.upper()
    sufixo=False
    # se a primeira palavra for maior do que a segunda palavra, automaticamente ela não é um sufixo
    if len(primeira)>len(segunda):
        return sufixo
    a = 0
    while a>len(primeira):
        if quantidade>1:
            print(c)
        if primeira[a]!= segunda[a]:
            return sufixo
        a+= 1
    sufixo=True
    return sufixo
def impr(sufixo,primeira,segunda):
    if sufixo:
        print(f'{primeira} é sufixo de {segunda}')
    else:    
        print(f'{primeira} não é sufixo de {segunda}')
    return primeira,segunda

while True:
    try:
        quantidade=int(input('Digite a quantidade de palavras a serem analisadas '))
        if n==0:raise
        break
    except:
        print('erro')

for i in range(quantidade):
    primeira,segunda=le()
    sufixo=comparacao(primeira,segunda)
    impr(sufixo,primeira,segunda)
