'''1. Faça um programa para ler 50 valores de temperaturas em graus Celsius.
Transformar essas temperaturas em Farenheit e imprimir a media das temperaturas
em Celsius e Farenheit e quantas temperaturas ficaram acima da media em Farenheit'''

temp=[]
Farenheit=[]
maiormedia=[]
cont=0
somafar=0
somatemp=0
def far(c):
    f=(9*c+160)/5
    return f
    
for i in range(1,5):
    temp.append(float(input(f'Digite a {i} temperatura em graus Celsius: ')))
print(22 * "= " )
for j in range(0,4):
    resultado = far(temp[j])
    somatemp+=temp[j]
    print(f'{temp[j]} Celsius é {resultado} Farenheit')
    Farenheit.append(resultado)
    somafar+=resultado
print(22 * "= " )
mediatemp=somatemp/5
mediafar=somafar/5
print(f'a media das temperaturas Celsius é {mediatemp} e a media das temperaturas Farenheit é {mediafar}')
print(22 * "= " )
for k in range(0,4):
    if Farenheit[k] > mediafar:
        maiormedia.append(Farenheit[k])
        cont+=1
print(f'existe {cont} temperaturas em Farenheit maiores do que {mediafar}')
print(f'as {cont} temperaturas são {maiormedia}')


