'''10. Uma empresa lançou um novo produto no mercado e fez uma pesquisa para saber
se os consumidores estavam satisfeitos, para isso eles deveriam responder sim ‘S’ ou
não ‘N’. Crie um algoritmo que leia a resposta de todas as pessoas e escreva a
porcentagem dos que disseram sim e dos que disseram não.
Obs: O final da leitura de dados é marcado pela resposta ‘F’.'''

#questao 10

quants=0
quantn=0
resposta=input('Você esta satisfeito com o produto (S/N): ')
while(resposta!='F') and (resposta!='f'):
    if (resposta=='s') or (resposta=='S'):
        quants+=1
    if (resposta=='n') or (resposta=='N'):
        quantn+=1
    print('='*40)
    resposta=input('Você esta satisfeito com o produto (S/N): ')
total=quants+quantn
porcn=(quantn*100)//total
porcs=(quants*100)//total
print('= ='*30)
print(f'a porcentagem de respostas SIM é {porcs}% e a porcentagem de respostas NÃO é {porcn}%')
