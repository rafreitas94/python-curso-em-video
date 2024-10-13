""" Jogo da Adivinhação v.1.0 """

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

computador = randint(0, 5)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

print(
    'PARABÉNS! Você conseguiu me vencer!' if computador == jogador else
    'GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
