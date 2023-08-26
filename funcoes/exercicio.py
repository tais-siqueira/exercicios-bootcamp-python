#Exercícios funções: 

#1: Faça um programa, com uma função que necessite de três argumentos e que forneça a soma desses três argumentos

def soma (num1,num2,num3):
    calculo = num1+num2+num3
    print(f'Resultado: {calculo}')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

soma(num1,num2,num3)

#2: Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127->721

numero = (input("Digite um número: ").upper())
invNumero = numero [::-1]

print('{}'.format(invNumero))

#3: Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius 
# para Fahrenheit ou vice-versa. Para cada opção, crie uma função. Crie uma terceira, que é um menu para 
# o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.

opcao = 0 

print('Escolha uma opção abaixo:')
opcao = int(input('[1] Celsius para Fahrenheit \n[2] Fahrenheit para Celsius\n'))

temperatura = float(input('Digite a temperatura: '))

if opcao == 1:
    calculo = (temperatura*1.8)+32
    print(f'O resultado é: {calculo:.1f}°F')

if opcao == 2:
    calculo = (temperatura-32)/1.8
    print(f'O resultado é: {calculo:.0f}°C')
