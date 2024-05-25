'''7. Um anagrama (do grego ana = "voltar" ou "repetir" + graphein = "escrever") é uma
espécie de jogo de palavras, resultando do rearranjo das letras de uma palavra ou
frase para produzir outras palavras, utilizando todas as letras originais exatamente
uma vez. Um exemplo conhecido é o nome da personagem Iracema, claro anagrama
de América, no romance de José de Alencar. Implemente a função anagrama(frase1,frase2). Os parâmetros frase1 e
frase2 são string. A função deverá retornar True se forem anagramas e False caso contrário.
Despreze acentuação (por exemplo: ã = a e ç = c) e os espaços não devem ser computados para efeitos do anagrama.'''




def anagrama(frase1,frase2):
    quant1=0
    quant2=0
    for k in range(0,(len(frase1)-1)):
        if frase1[k]!= ' ':
            quant1+=1
        if frase1[k] == 'ã':
            frase1[k] = 'a'
        if frase1[k] == 'ç':
            frase1[k] = 'ç'
        if frase1[k] == 'é':
            frase1[k] = 'e'

            
    for y in range(0,(len(frase2)-1)):
        if frase1[y]!= ' ':
            quant2+=1
        if frase1[y] == 'ã':
            frase1[y] = 'a'
        if frase1[y] == 'ç':
            frase1[y] = 'ç'
        if frase1[y] == 'é':
            frase1[y] = 'e'

        
    if quant1==quant2:
        for i in range(0,(len(frase1))):
            for j in range(0,(len(frase2))):
                if frase1[i] == frase2[j]:
                    frase1 = frase1.replace(frase1[i],'*')
                    frase2 = frase2.replace(frase2[j],'*')
    if frase1 == ((quant1+1)*'*'):
        resultado=True
    else:
        resultado=False
    return resultado
                    
            
frase1= str(input('Digite a primeira palavra: '))
frase2= str(input('Digite a segunda palavra: '))
print('= '*10)
if anagrama(frase1,frase2) == True:
    print(f'A palavra {frase1} e {frase2} são anagramas')
else:
    print(f'A palavra {frase1} e {frase2} NÃO são anagramas')
    
