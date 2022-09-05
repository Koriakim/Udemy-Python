# 1. Faça um programa que leia um número inteiro e o imprima.
num_int = int(10)
print(f'Numero inteiro é: {num_int}')
print(' ')
# 2. Faça um programa que leia um número real e o imprima.
num_real = float(10)
print(f'Numero real é: {num_real}')
print(' ')
# 3. Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
print('Atividade soma números inteiros!!!')
num_int1 = int(input('Digite o primeiro numero inteiro: '))
num_int2 = int(input('Digite o segundo numero inteiro: '))
num_int3 = int(input('Digite o terceiro numero inteiro: '))
soma = num_int1 + num_int2 + num_int3
print(f'A soma dos números inteiros {num_int1},{num_int2} e {num_int3} é:', soma)
print(' ')
# 4. Leia um número real e imprima o resultado do quadrado desse número.
num_real = 10.0
print(num_real**2)
print(' ')
# 5. Leia um número real e imprima a quinta parte desse número.

# 6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é:
# F = C*(9.0/5.0)+32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
temperatura_Cel = 20
convert_Fah = temperatura_Cel*(9.0/5.0)+32.0
print(f'Temperatura em celsius é de {temperatura_Cel}ºC, em Fahrenheit é de {convert_Fah}ºFah.')
print(' ')
# 7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A fórmula de conversão é:
# C = 5.0*(F-32.0)/9.0, sendo C a temperatura em Celsius e F em Fahrenheit.
temperatura_Fah = 68
convert_Cel = float(5.0*(temperatura_Fah-32.0)/9.0)
print(f'Temperatura em Fahrenheit é de {temperatura_Fah}ºFah, em Celsius é de {convert_Cel}ºC.')
print(' ')
# 8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão
# é: C = K-273.15
temperatura_Kel = 293.15
convert_Kel = temperatura_Kel-273.15
print(f'Temperatura em kelvin é de {temperatura_Kel}ºKel, em Celsius é de {convert_Kel}ºC.')
print(' ')
# 9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A fórmula de conversão
# é: K = C + 273.15
temperatura_Cel2 = 20
convert_kel2 = temperatura_Cel2 + 273.15
print(f'Temperatura em Celsius é de {temperatura_Cel}ºC, em Fahrenheit é de {convert_kel2}')
print(' ')
# 10. Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo). A fórmula
# de conversão é: M = K/36, sendo, K a velocidade em km/h e M em m/s.
velo_km = 100
convert_ms = velo_km/3.6
print(f'A velocidade em KM/H é de {velo_km}km/h, em M/S é de {convert_ms}m/s.')
print(' ')
# 11. Leia uma velocidade em m/s e apresente-a convertida em km/h. A fórmula de conversão é de: K = M*3.6.
velo_ms = 27
convert_km = velo_ms*3.6
print(f'A velocidade em M/S é de {velo_ms}m/s, em KM/H é de {convert_km}')
