'''13. Crie a função multiplica_matriz(mat1, mat2) que deve retornar o produto de duas
matrizes bidimensionais genéricas, sem alterar as matrizes originais. A função deve
imprimir uma mensagem de erro e retornar um vetor vazio ([]) caso não for possível
realizar o produto das duas matrizes.'''


def cria_matriz(vet,x,y):
    for i in range(x):
        vet.append(0)
        vet[i] = []
        for j in range(y):
            vet[i].append(int(input('Entre com Elemento da matriz:')))



def imprime(mat,x,y):
   for i in range(x):
        for j in range(y):
           print('| ', mat[i][j], end = '  ')
        print('|')



def analise_mats(n_colunas1,n_linhas2):
    if n_colunas1 == n_linhas2:
        return True
    else:
        return False



def multiplica_matriz(vet1,vet2):
    if analise_mats(c1,l2):
        new_mat = []
        for i in range(l1):
            new_mat.append(0)
            new_mat[i] = []
            for j in range(c2):
                soma1 = soma2 = soma3 = 0
                for a in range(c1):
                    soma1 += vet1[i][a]*vet2[a][i]
                    soma2 += vet1[i][a]*vet2[a][i+1]
                    soma3 += vet1[i][a]*vet2[a][j]
                new_mat[i].append(soma1)
                new_mat[i].append(soma2)
                new_mat[i].append(soma3)
        return new_mat
    else:
        print('ERRO!!')
        mat0 = []
        return mat0

    
mat1 = []
mat2 = []


l1 = int(input('Entre com n. de linhas:'))
c1 = int(input('Entre com n. de colunas:'))

cria_matriz(mat1,l1,c1)

l2 = int(input('Entre com n. de linhas:'))
c2 = int(input('Entre com n. de colunas:'))

cria_matriz(mat2,l2,c2)
imprime(mat1,l1,c1)

print()

imprime(mat2,l2,c2)

print()

imprime(multiplica_matriz(mat1,mat2),l1,c2)



