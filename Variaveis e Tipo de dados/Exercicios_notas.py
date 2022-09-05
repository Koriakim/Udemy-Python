# 29. Leia quatro notas, calcule a média aritmética e imprima o resultado

nota1 = int(input('Insira a primeira nota: '))
nota2 = int(input('Insira a segunda nota: '))
nota3 = int(input('Insira a terceira nota: '))
nota4 = int(input('Insira a quarta nota: '))

total = (nota1 + nota2 + nota3 + nota4)

soma = total / 4

if soma >= 6:
    print("Você passou!!!")
else:
    print('Reprovado')

print(f'A sua média é: {soma}')
