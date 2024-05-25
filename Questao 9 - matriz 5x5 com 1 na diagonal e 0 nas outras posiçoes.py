'''9. Crie uma matriz 5x5 com 1 na diagonal principal e 0 nas outras posições. Imprima a
matriz no formato tradicional de linhas e colunas'''


def criavet(vet):
    for i in range(0,5):
        mat.append(0)
        mat[i] = [0,0,0,0,0]
        for j in range(0,5):
            if i == j:
                mat[i][j] = 1
            else:
                mat[i][j] = 0
            

def imprime(vet):
    for i in range(0,5):
        for j in range(0,5):
            print(mat[i][j], end = ' ')
        print()

mat = []
criavet(mat)
imprime(mat)
