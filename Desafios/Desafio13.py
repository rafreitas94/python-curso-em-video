n1 = float(input('Digite o seu salário: R$'))
d = n1*(15/100)
t = n1 + d
print('O aumento será de R${:.2f}. O salário total é R${:.2f}.'.format(d, t))
