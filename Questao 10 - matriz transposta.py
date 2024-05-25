'''10. Crie a função mat_transposta(matriz). A função deve receber uma matriz genérica
bidimensional, de qualquer tamanho (não necessariamente quadrada) e retornar a
matriz transposta, sem alterar a matriz original.'''


def cria_mat(mat1,a,b,aux):
    for i in range(0, a):
        mat1.append(0)
        mat1[i] = []
        for j in range(0, b):
            mat1[i].append(int(input('elementos da matriz:')))
            aux.append(mat1[i][j])
    print()


    
def criatransmat(mat2,a,b,aux):
    for i in range(0, b):
        mat2.append(0)
        mat2[i] = []
        for j in range(0, a):
            mat2[i].append(aux[j][i])




            
def imprime(mat,mat2,a,b):
    for i in range(0, a):
        for j in range(0, b):
            print('|', mat[i][j], end = ' ')
        print('|')
    print()
    for i in range(0, b):
        for j in range(0, a):
            print('|', mat2[i][j], end = ' ')
        print('|')



        
mat1 = []
mat2 = []
aux = []


a = int(input('Entre com n. de linhas da primeira mat:'))
b = int(input('Entre com n. de colunas da primeira mat:'))

print()


cria_mat(mat1,a,b,aux)
criatransmat(mat2,a,b,mat1)
imprime(mat1,mat2,a,b)
