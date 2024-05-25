magro=0
gordo=0
quantidade=0
quantn=0
quantg=0
quanto=0

peso=input('Digite o peso: ')
while(peso!=''):
    peso=float(peso)
    raca=input('Digite a raça (N/G/O): ')
    if (raca != 'N') or (raca != 'n') or (raca != 'g') or (raca != 'G') or (raca != 'o') or (raca != 'O'):
        while (raca != 'N') and (raca != 'n') and (raca != 'g') and (raca != 'G') and (raca != 'o') and (raca != 'O'):
            print('*** ERRO!!! ***')
            raca=input('Digite a raça (N/G/O): ')
    print('='*20)
    quantidade+=1
    if quantidade == 1:
        gordo=peso
        magro=peso
    if peso>gordo:
        gordo=peso
    if peso<magro:
        magro=peso
    if (raca == 'N') or (raca == 'n'):
        quantn+=1
    if (raca == 'g') or (raca == 'G'):
        quantg+=1
    if (raca == 'O') or (raca == 'o'):
        quanto+=1
    peso=input('Digite o peso: ')
print(f'o boi mais magro tem {magro}kg')
print(f'o boi mais gordo tem {gordo}kg')
print(f'existe {quantn} bois n')
print(f'existe {quantg} bois g')
print(f'existe {quanto} bois o')
