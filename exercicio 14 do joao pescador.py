peso= float(input('quantos kg vc trouxe: '))

excesso= peso-50
multa= (excesso*4)

if(peso>50):
    print('o excesso de kg é de',excesso)
    print('pagará uma multa de R${:.2f}'.format(multa))
else:
    print('nao tera excess de kg e nao pagara multa')
