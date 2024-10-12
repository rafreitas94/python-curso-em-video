""" Aula 09 - Curso em Video """
frase = "Curso em Vídeo Python"
fraseComEspaco = "   Curso em Vídeo Python   "

print('Exibe a frase: ', frase)

print('Exibe um pedaço: ', frase[3:13])

print('Da letra 1 até a 15', frase[1:15])

print('Da letra 1 até a 15 a cada 2: ', frase[1:15:2])

# Exibe um texto longo
print("""Lorem Ipsum is simply dummy text of the printing and typesetting
industry. Lorem Ipsum has been the industry's standard dummy text ever since
 the 1500s, when an unknown printer took a galley of type and scrambled it
 to make a type specimen book. It has survived not only five centuries, but
  also the leap into electronic typesetting, remaining essentially unchanged.
   It was popularised in the 1960s with the release of Letraset sheets
    containing Lorem Ipsum passages, and more recently with desktop publishing
     software like Aldus PageMaker including versions of Lorem Ipsum.""")

print('Conta quantos "o" existem: ', frase.count('o'))

print('Contando espaço: ', len(fraseComEspaco))

print('Realiza replace: ', frase.replace('Python', 'Android'))

# Verifica se curso está dentro de frase
print('Curso' in frase)

# Verifica palavra curso e exibe em qual posição está
print(frase.find('Vídeo'))

print('Exibe a frase em lista: ', frase.split())

print('Exibe apenas Vídeo através de uma lista: ', frase.split()[2])
