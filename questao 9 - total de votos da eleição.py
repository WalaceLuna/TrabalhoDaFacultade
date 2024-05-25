'''9. Crie um algoritmo que apure os votos de uma eleição municipal, numa cidade com
20.000 eleitores, onde concorreram quatro candidatos. Um servidor da Justiça
Eleitoral digitará cada voto individualmente. Cada voto equivale a um número inteiro.
Os votos válidos podem ser 1, 2, 3 e 4, e estão relacionados aos seguintes candidatos:
1 – João da Silva
2 – José Ramalho
3 – Maria Mattos
4 – Pedro Américo
Votos com o valor 0 devem ser contabilizados como votos em branco, e votos com
qualquer outro valor (além de 0, 1, 2, 3 e 4), devem se considerados votos nulos.
Calcule e escreva o total de votos de cada candidato, o total de votos brancos e o total
de votos nulos.'''

#questao 9

v0=0
v1=0
v2=0
v3=0
v4=0
vn=0
for i in range(1,7):
    voto=int(input(f'Digite o voto do {i} eleitor: '))
    if(voto==0):
        v0+=1
    if(voto==1):
        v1+=1
    if(voto==2):
        v2+=1
    if(voto==3):
        v3+=1
    if(voto==4):
        v4+=1
    if(voto!=0)and(voto!=1)and(voto!=2)and(voto!=3)and(voto!=4):
        vn+=1
    print('='*25)
print(f'João da Silva teve {v1} votos')
print('='*25)
print(f'José Ramalho teve {v2} votos')
print('='*25)
print(f'Maria Mattos teve {v3} votos')
print('='*25)
print(f'Pedro Américo teve {v4} votos')
print('='*25)
print(f'tiveram {v0} votos em branco')
print('='*25)
print(f'tiveram {vn} votos nulos')
print('='*25)
