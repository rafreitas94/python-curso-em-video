n1 = float(input('Digite a largura da parede em metros(em m): '))
n2 = float(input('Digite a altura da parede em metros(em m): '))
a = n1 * n2
qtde = a/2
print('Área calculada (em m²): {:.1f}m²'.format(a))
print('Quantidade de tinta necessária (em litros): {:.1f}l'.format(qtde))
