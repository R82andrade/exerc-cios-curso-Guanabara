from random import randint
computador = randint (0, 10)# faz o computador "PENSAR"
print ('_=_'*20)
print('Vou pensar em um número entre 0 e 10. Tente Adivinha...')
print ('_=_ '*20)
jogador = int(input('Em que número eu pensei?')) # jogador adivinhar
if jogador == computador:
    print('PARABÉNS!você conseguiu me vencer!!!')
else:
    print('GANHEI!Eu ganhei {} e não no {}!' .format(computador, jogador))