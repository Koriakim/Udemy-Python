# Faça um algoritmo que calcule o I M C de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:
def IMC():
    print('Exercicio de calculo IMC:')

    altura = float(input('Insira a sua altura: '))
    peso = float(input('Insira o seu peso: '))

    imc = peso / (altura * altura)

    if imc < 18.5:
        print(f'O seu IMC é {imc:.2f}. Abaixo do peso.')
    elif imc <= 24.9:
        print(f'O seu IMC é {imc:.2f}. Saudavel')
    elif imc <= 30:
        print(f'O seu IMC é {imc:.2f}. Peso em excesso')
    elif imc <= 34.9:
        print(f'O seu IMC é {imc:.2f}. Obesidade Grau 1')
    elif imc <= 39:
        print(f'O seu IMC é {imc:.2f}. Obesidade Grau 2 (Severa)')
    elif imc > 40:
        print(f'O seu IMC é {imc:.2f}. Obesidade Grau 3 (Mórbida)')
    else:
        print('Insira corretamente o numero'), IMC()


IMC()
