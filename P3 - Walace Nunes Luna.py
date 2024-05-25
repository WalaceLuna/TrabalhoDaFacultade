
def le():
    n=int(input('Digite o número de linhas: '))
    m=int(input('Digite o número de colunas: '))
    if m==n:
        m=int(input('**ERROR** POR FAVOR, DIGITE UM NÚMERO DIFERENTE DE LINHAS: '))

    a=[None]*n
    for i in range(n):
        a[i]=[None]*m
        for j in range(m):
            a[i][j]=int(input(f'Digite A ({i+1},{j+1}) --> '))

    b=[None]*n
    for l in range(n):
        b[l]=[None]*m
        for c in range(m):
            b[l][c]=int(input(f'Digite B ({l+1},{c+1}) --> '))

    c=[None]*n
    for d in range(n):
        c[d]=[None]*m
        for k in range(m):
            c[d][k]=int(input(f'Digite c ({d+1},{k+1}) --> '))
            
    return a, b, c

def impr(a, b, c):    
    print (f"\n{'Matriz Lida':*^30}")
    for i in range(3):
        for j in range (3):
            print (f'{a[i][j]:>10}')
        print()
    for l in range(3):
        for c in range (3):
            print (f'{a[l][c]:>10}')
        print()
    for d in range(3):
        for k in range (3):
            print (f'{a[d][k]:>10}',end=' ')
        print()
    return
    
a, b, c=le()
impr(a, b, c)
