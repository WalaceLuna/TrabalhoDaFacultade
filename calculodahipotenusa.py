from math import*
cateto1= float(input('Qual o valor do cateto 1: '))
cateto2= float(input('Qual o valor do cateto 2: '))

cateto1= cateto1 ** 2
cateto2= cateto2 ** 2

hipotenusa= sqrt(cateto1+cateto2)

print('A hipotenusa do \t triangulo retângulo é {:.2f}'.format(hipotenusa))
