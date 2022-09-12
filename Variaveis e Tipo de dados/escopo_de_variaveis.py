"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Varáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Varáveis locai:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está lomitado
    ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_varuavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável,
nós não colocamos o tipo de dado dela.
E   sse tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C:

int numero = 42;

Exemplo em java:

int numeri = 42;
"""

numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existo = 'Oi'
print(nao_existo)

# Exemplo de variavel Local:


def novo():
    if numero > 10:
        soma = numero + 10
        print(soma)


# A variavel "soma" foi declarado somente dentro no bloco da função "novo()", então não podemos utilizar fora do bloco da função.
# print(soma)
