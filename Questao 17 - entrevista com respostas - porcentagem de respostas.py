'''17. Uma certa firma fez uma pesquisa para saber se as pessoas gostaram ou não de um
novo produto lançado no mercado. Para isso, forneceu o sexo do entrevistado e sua
resposta (sim ou não). Sabendo-se que foram entrevistadas 2.000 pessoas, crie um
algoritmo que calcule e escreva:

a) o número de pessoas que responderam sim;

b) o número de pessoas que responderam não;a porcentagem de pessoas do
sexo masculino que responderam não'''


m=[]

def contagem(respostas):
    conts=0
    for i in range(a,len(respostas)):
        if(respostas[i] == 's' or (respostas[i] == 'S')):
            conts+=1
    print('Numero de pessoas que respondeu "sim": ', conts)

for i in range(0,5):
    resp=input('Voce gostou do nosso produto (s/n): ')
    while(resp != 's') and (resp != 'S') and (resp != 'n') and (resp != 'N'):
        print('***ERRO*** RESPOSTA ERRADA')
    resp=input('Voce gostou do nosso produto (s/n): ')
    m.append(resp)
contagem(m)
