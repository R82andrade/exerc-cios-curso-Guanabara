# Analisador de Textos

nome = str (input('Digite seu nome completo:')).strip()
print ('Analisando seu nome...')
print('Seu nome masiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format( nome.lower ()))
print ('Seu nome ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print(' Seu primeiro nome tem {} letras'.format(nome.find ('  ')))