codigo=float(input('informe o codigo: '))
preço=float(input('informe o valor: '))

desconto= (10*preço)/100

if(codigo == 00):
    print('valor final:',(preço - desconto))
else:
    print('valor final:',preço)
