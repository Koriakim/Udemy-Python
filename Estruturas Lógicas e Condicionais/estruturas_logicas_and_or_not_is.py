"""
Estrututas lógicas: and (e), or (ou), not (não) e is (é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is
"""
import numbers
from turtle import title
from unicodedata import numeric


ativo = True
logado = False

if not ativo:
    print('Bem vindo!!!')
else:
    print('Ative o seu e-mail!!!')

if not logado:
    print('O seu usuario já está logado em outra seção!!!')
else:
    print('Realiza o loguin!!!')

if ativo and logado:
    print('Bem vindo!!!')
else:
    print('Realizar o loguin')

if ativo or logado:
    print('Bem vindo!!!')
else:
    print('Realizar o loguin')

if ativo is True:
    print('Usuario ativo')
else:
    print('Ativar o seu loguin')

if logado is True:
    print('Usuario já logado!')
else:
    print('Inicie a sua seção!!!')

perg = input('Digite alguma coisa: ')

if perg is str:
    print('Você digitou uma string!!!')
else:
    print('Você digitou um numero')
