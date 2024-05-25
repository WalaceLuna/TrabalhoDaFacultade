metrosquadrados= int(input('Qual o tamanho da area em metros quadrados que sera pintada: '))

litrosusados= float(metrosquadrados / 3)

umalata=18
valordalata= 80

quantidadedelatas= int(litrosusados / 18)

resto= litrosusados % 18

if(litrosusados <= umalata):
    print('precisará de uma lata de tinta')
    print('pagará R${:.2f}'.format(valordalata))
else:
    if(resto == 0):
        print('precisará de',quantidadedelatas,'latas de tintas')
        print('pagará R${:.2f}'.format(quantidadedelatas*80))
    else:
        print('precisará de',(quantidadedelatas + 1),'latas de tintas')
        print('pagará R${:.2f}'.format((quantidadedelatas + 1)*80))
        
        
