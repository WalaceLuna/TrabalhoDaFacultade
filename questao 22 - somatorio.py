'''22. Crie um algoritmo que leia um número N e calcule:
∑
1
𝑖
𝑁
𝑖=1
:
'''

#questao 22

soma=0
n=int(input('Digite um numero: '))
for i in range(1,n):
    soma+=1/i
print(soma)
