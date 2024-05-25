'''3. Leia uma frase e imprima o total de vogais, o total de brancos e o total do resto.'''

quantesp=0
quantvog=0
quantrest=0

frase=(input('Digite uma frase: '))
for i in range(0,len(frase)):
    if frase[i]==" ":
        quantesp+=1
    elif frase[i]=="a" or frase[i]=="A" or frase[i]=="e" or frase[i]=="E" or frase[i]=="i" or frase[i]=="I" or frase[i]=="o" or frase[i]=="O" or frase[i]=="u" or frase[i]=="U":
        quantvog+=1
    else:
        quantrest+=1
print(f'existem {quantvog} vogais, {quantesp} espaços e {quantrest} resto')


