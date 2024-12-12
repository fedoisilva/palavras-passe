import random

print('BEM VINDO AO PALAVRAS-PASSE. SEU GERADOR DE SENHAS SEGURAS')      

input('Pressione ENTER para gerar sua senha: ')

senha = [] 

def gerar_numero():
    numero = chr(random.randint(48,57))
    senha.append(numero)

def gerar_letra_maiuscula():
    letra_maiuscula = chr(random.randint(65,90))
    senha.append(letra_maiuscula)

def gerar_letra_minuscula():
    letra_minuscula = chr(random.randint(97,122))
    senha.append(letra_minuscula)

def gerar_caractere():
    caractere = chr(random.randint(35,38))
    senha.append(caractere)


for i in range(4):
    gerar_letra_maiuscula()

for i in range(4):
    gerar_letra_minuscula()           

for i in range(2):
    gerar_numero()

for i in range(2):
    gerar_caractere()

random.shuffle(senha)
senha = ''.join(senha)

print(f'''
Sua senha gerada é:

{senha}

Copie-a e cole em um local seguro.
''')

