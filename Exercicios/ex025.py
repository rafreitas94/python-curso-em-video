""" Procurando uma string dentro de outra """

nome = str(input("Inform seu nome completo: ")).strip().lower()

print('Seu nome tem Sousa? {}'.format('sousa' in nome))
