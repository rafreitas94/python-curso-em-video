n1 = float(input('Digite o preço do produto: R$'))
d = n1*(5/100)
t = n1 - d
print('O desconto é de R${:.2f}. O preço final é R${:.2f}.'.format(d, t))
