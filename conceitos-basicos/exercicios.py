#Conceitos básicos:

#1: Faça um Programa que peça um número e então mostre a mensagem: -> Onúmero informado foi [número]

numero = (input('Digite um número: '))

print(f'O número informado foi: {numero}')

#2: Faça um Programa que peça dois números e imprima a soma

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))

soma = numero1+numero2
print(f'A soma dos números é: {soma}')

#3: Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit

numero = int(input('Digite a temperatura em Celsius: '))

mult = numero*1.8
soma = mult+32

print(f'A temperatura em Fahrenheit é: {soma:.1f} graus')

#4: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

numero1 = float(input('Digite quanto você ganha por hora: '))
numero2 = int(input('Digite o número de horas trabalhadas por mês: '))

mult = numero1*numero2

print(f'O seu salário é de: {mult} reais')



