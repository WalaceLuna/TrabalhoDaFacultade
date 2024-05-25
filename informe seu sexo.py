sexo=str(input('informe seu sexo: [M/F] '))
while(sexo not in 'MmFf'):    
    sexo=str(input('Dados invalidos. Por favor, informe seu sexo: [M/F] '))
print('sexo {} registrado com sucesso'.format(sexo))
