'''15. Escreva uma função para condensar os elementos de uma lista ordenada L, que
contém inteiros repetidos. Por exemplo, para L = [3, 3, 3, 3, 7, 7, 13, 13, 23], a função
retorna ['3^4', '7^2', '13^2', '23'] (repare que são strings). Note-se que no caso de um
número aparecer uma única vez, não deve haver expoente unitário.'''


def busca(buscado,a):
    for i in range(len(a)):
        if buscado == a[i]:
           return i
    return -1




def vet_sem_rap(lista,a,b):
    for i in range(len(lista)):
        posicao = busca(str(lista[i]),a)
        if (posicao != -1):
            b[posicao] += 1
        else:
            a.append(str(lista[i]))
            b.append(1)



            
def cria_lista(lista,vetor_id):
    new_list = []
    for i in range(len(lista)):
        if (vetor_id[i] > 1):
            new_list.append(str(lista[i]) + '^' + str(vetor_id[i]))
        else:
            new_list.append(str(lista[i]))
    return new_list




lista_sem_rap = []
lista_ind = []
L = [3, 3, 3, 3, 7, 7, 13, 13, 23]
vet_sem_rap(L,lista_sem_rap,lista_ind)


print(lista_sem_rap)
print(lista_ind)
print(cria_lista(lista_sem_rap,lista_ind))
