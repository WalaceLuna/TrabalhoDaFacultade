'''18. Crie um algoritmo que leia um número N e verifique se ele é primo. O seu
programa deve fazer o MÍNIMO de interações possíveis.'''


def primo(numero):
    primo=True
    for i in range(2,n):
        if(n % i == 0):
            primo = False
    if(primo == True):
        print('Este Número é primo')
    else:
        print('Este Número não é primo')

n=int(input('Insira um numero n para ver se ele é primo: '))
primo(n)
