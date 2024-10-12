""" Crie um programa que leia o nome completo de uma pessoa e mostre: """
nome = str(input("Digite seu nome completo: "))

print("O nome com todas as letras maiúsculas: ", nome.upper())

print("O nome com todas as letras minúsculas: ", nome.lower())

print("Quantas letras ao possui (sem considerar espaços): {}".format(len(nome.strip()) - nome.count(' ')))

print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.strip().split()[0], len(nome.strip().split()[0])))
