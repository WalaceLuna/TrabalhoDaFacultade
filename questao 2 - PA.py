'''2. Crie um algoritmo que escreva os N primeiros termos de uma progressão aritmética
(PA). O primeiro termo e a razão da PA devem ser informados pelo usuário'''

#questao 2

n=5
termo=int(input('Digite o numero que começarar a ser lidos: '))
pa=int(input('Digite a quantidade de numeros a serem pulados: '))
print(termo)
for i in range(1,n):
    termo=termo+pa
    print(termo)
