"""
Calculadora de imc
pesos ideais desde o minimo até o maximo
min_normal = 18.5
max_normal = 24.9
acima_min = 24.0
acima_max = 29.9
obeso_min = 30.0
obeso_max = 34.9
obeso_min = 35
obeso_max = 39.9
"""
print('Bem vindo a Calculadora de IMC: ')
print()

nome = input('Digite seu Nome: ')
idade = input('Informe Sua Idade: ')
peso = float(input('Informe seu Peso: '))
altura = float(input('Informe Sua Altura: '))
imc = (peso / altura ** 2)

min_normal = 18.5
max_normal = 24.9
acima_min = 24.0
acima_max = 29.9
obeso_min = 30.0
obeso_max = 34.9
obeso_min2 = 35
obeso_max2 = 39.9

print()

print(f'{nome} tem {idade} anos de idade, pesa {peso} kg e mede {altura} metros de altura.'
      f' Seu imc é igual a: {imc:.2f}')
if imc >= min_normal and imc <= max_normal:
    print(f'O peso do(a) {nome} é normal')
elif imc >= acima_min and imc <= acima_max:
    print(f'{nome} Está acima do Peso')
elif imc >= obeso_min and imc <= obeso_max:
    print(f'{nome} Está com obesidade')
elif imc >= obeso_min2 and imc <= obeso_max2:
    print(f'{nome} Está com uma taxa de obesidade severa')
else:
    print()
print('Para saber qual seria o seu peso ideal, favor digite os dados a seguir: ')

altura_ideal = int(input('Favor digite novamente a altura sem utilizar o ponto(.): '))
sexo = input('Informe seu Sexo: ')
peso_ideal_masc = 52 + (altura_ideal - 152.4) * 0.75
peso_ideal_fem = 52 + (altura_ideal - 152.4) * 0.67
peso_ideal_ajst_fem = ((peso - peso_ideal_fem) * 0.25) + peso_ideal_fem
peso_ideal_ajst_masc = ((peso - peso_ideal_masc) * 0.25) + peso_ideal_masc
if sexo == ('masculino'):
    print(f'O peso ideal de {nome} seria {peso_ideal_masc:.2f}')
    print(f'o peso ideal ajustado {nome} seria {peso_ideal_ajst_masc:.2f}')
elif sexo == ('feminino'):
    print(f'O peso ideal de {nome} seria o {peso_ideal_fem:.2f}')
    print(f'O peso ideal ajustado de {nome} seria {peso_ideal_ajst_fem:.2f}')
else:
    print()
print('OBRIGADO POR UTILIZAR NOSSA CALCULADORA IMC, ESPERO QUE CONCIENTIZE EM RELAÇÃO A SUA SAÚDE')