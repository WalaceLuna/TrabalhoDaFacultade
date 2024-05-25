'''6. Um palíndromo é uma cadeia que pode ser lida de frente para trás e de trás para
frente. Ex: ‘SOMOS’ ‘1234321’. Implemente a função palindromo(palavra). O
parâmetro palavra é uma string. A função deverá retornar True se for um palíndromo e
False caso contrário.'''

nome= input('Digite um nome: ')
for i in range(1,len(nome)):
     if nome[i-1] == (nome[len(nome)-i]):
          resultado='true'
     else:
        resultado='false'
        break
        
if resultado == 'true':
    print(resultado)
if resultado == 'false':
    print(resultado)
