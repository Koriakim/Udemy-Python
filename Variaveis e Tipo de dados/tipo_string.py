"""
Tipo String

- Estiver entre áspas simples -> 'uma string', '234', 'a', 'True', '42.3';
- Estiver entre áspas duplas -> "uma string", "234", "a", "True", "42.3";
- Estiver entre áspas triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3''';
"""
# - Estiver entre áspas duplas triplas -> """uma string""", """234""", """ a """, """True""", """42.3"""

from cgitb import text


nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = 'Angelina \" Jolie'
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split())  # Transforma em uma lista de strings

nome = 'Geek University'
print(nome[0:4])  # Slice de string

print(nome[5:15])  # Slice de string

# Geek
print(nome.split()[0])
# University
print(nome.split()[1])

print(nome[::-1])

print(nome.replace('G', 'P'))

texto = 'socorram me subino oninus em marrocos'

print(texto)

print(texto[::-1])
