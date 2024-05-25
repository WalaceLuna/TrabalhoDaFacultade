from math import*
a= float(input('Qual o valor de a: '))
b= float(input('Qual o valor de b: '))
c= float(input('Qual o valor de c: '))

x1=(-b + (sqrt((b)**2 - (4*(a)*(c)))))/(2*(a))
x2=(-b - (sqrt((b)**2 - (4*(a)*(c)))))/(2*(a))

print('O valor da equação é',x1,'e',x2)
