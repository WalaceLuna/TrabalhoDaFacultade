def main():
    quantidade=0
    totalN=0
    totalG=0
    totalO=0
    gordo=None
    magro=None
    while True:
        peso=input('Qual o peso do boi: ')#perguntando o peso do boi
        if peso =='':break #quando quiser parar é só dá enter que o programa vai para o resultado
        peso=float(peso)#transformando os valores de peso em numero com virgula
        quantidade+=1 #calculando a quantidade de bois lida
        #vendo agora os bois mais pesados e mais leve ao total
        if quantidade==1:
            gordo=magro=peso
        elif peso>gordo:      
            gordo=peso
        elif peso<magro:
            magro=peso
       #agora para ler as raças
        raça=leraça()
        if raça=='N':
            totalN+=1
        elif raça=='G':
            totalG+=1
        elif raça=='O':
            totalO+=1
    return gordo,magro,totalN,totalG,totalO,quantidade       
def leraça():
    while True:
        raça=input('Qual a raça do boi (N,G ou O): ').strip().upper()#perguntando a raça do boi e em seguida tranformando a resposta em letra maiuscula
        if raça=='N' or raça=='G' or raça=='O':
            return raça
        else:
            print('digitar novamente')#se o boi digitado nao for N,G ou O o pramaga pede para digitar novamente
def impr(gordo,magro,totalN,totalG,totalO,quantidade):
    if quantidade==0:
        print('não existe nenhum boi') #caso a quantidade seja zero, o programa dira que nao existe boi
    else:    
        print(f'O boi mais gordo tem {gordo:.2f} kg') #dira qual o boi mais pesado
        print(f'O boi mais magro tem {magro:.2f} kg') #dira qual o boi mais leve
        if totalN==0:
            print('Não existem bois da raça nelore') #se nao existir bois nelore, o programa dira que nao ixiste
        else:
            print(f'Existem {totalN} bois nelore') #se existir bois nelore, o programa dira a quantidade de bois
            
        if totalG==0:
            print('Não existem bois da raça giroles') #se nao existir bois girole, o programa dira que nao ixiste
        else:
            print(f'Existem {totalG} bois da raça giroles') #se existir bois gitole, o programa dira a quantidade de bois
        if totalO==0:
            print('Não existem bois de outras raça') #se nao existir bois de outras raças, o programa dira que nao ixiste
        else:
            print(f'Existem {totalO} bois de outra raça')  #se existir bois de outra raças , o programa dira a quantidade de bois  
# principal            
gordo,magro,totalN,totalG,totalO,quantidade=main()
impr(gordo,magro,totalN,totalG,totalO,quantidade)
    
