maior=0
menor=0
for c in range(1,6):
    peso=float(input('Digite o {}º peso: '.format(c)))
    if(c == 1):
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso é ',maior)
print('o menor peso é ',menor)
            
