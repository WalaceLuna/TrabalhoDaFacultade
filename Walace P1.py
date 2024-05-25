quantidade=int(input('Quantos bois deseja registra: '))
maisgordo=0
maismagro=0

if quantidade == 0:
    print('Dados inválidos. Não foi possivel registrar.' )
    

for c in range(quantidade):
    peso=float(input('Insira o peso do boi: '))

for R in range(quantidade):   
    raça=str(input('Digite a raça do boi [N,G ou O]: '))
    while(raça not in 'nNgGoO'):
        raça=str(input('Dados inválidos. Por favor, informe a raça do boi: '))
if(c == 1):
    maisgordo = peso
    maismagro = peso
else:
     if peso > maisgordo:
         maisgordo = peso
     if peso < maismagro:
            maismagro = peso
print('O mais gordo é ',maisgordo)
print('O mais magro é ',maismagro)
