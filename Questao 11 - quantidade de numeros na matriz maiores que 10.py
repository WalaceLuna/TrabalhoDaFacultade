'''11. Crie a função mat_maior_10(matriz). A função deve receber uma matriz genérica,
de qualquer tamanho (não necessariamente quadrada) e retornar a quantidade de
elementos da matriz maiores que dez.'''


def gerar_matriz (mat,n_linhas, n_colunas):
    for i in range(n_linhas):
        mat.append([])
        for j in range(n_colunas):
            mat[i].append(int(input('Elem. matriz:')))
    return mat


def imprime(mat,x,y):
    for i in range(x):
        for j in range(y):
            print(mat[i][j], end = ' ')
        print()

        
def mat_maior_10(matriz,x,y):
    cont = 0
    for i in range(x):
        for j in range(y):
            if matriz[i][j] > 10:
                cont += 1
    return cont



mat =[]


l = int(input('Entre com n. de linhas da primeira mat:'))
c = int(input('Entre com n. de colunas da primeira mat:'))


gerar_matriz(mat,l,c)
imprime(mat,l,c)


print('Temos {} elementos maiores que 10 na matriz'.format(mat_maior_10(mat,l,c)))
