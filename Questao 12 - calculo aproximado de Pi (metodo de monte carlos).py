'''12. Cálculo aproximado de ∏ (Pi) pelo Método de Monte Carlo.
Dada a função


x^2 + y^2 <= 4


calcule o valor aproximado de ∏ com 4.10^6 interações.

Dicas: use random.random()*2 para gerar valores
entre 0 e 2 para as variáveis x e y e conte o número de pontos (x,y)
que satisfazem a equação dada e divida o resultado por 10^6
Cuidado com o tipo de dados.'''

import random

contD = 0
contF = 1

for i in range(0,100):
    x = 2*random.random()-1
    y = 2*random.random()-1
    z = (x**2)+(y**2)
    print(z)
    if z <= 2:
        contD += 1
    else:
        contF += 1 

pi = 4*(contD/contF)
print('Pi:', pi)
