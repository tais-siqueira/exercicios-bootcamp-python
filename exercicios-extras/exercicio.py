#1: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, 
# e calcule quanto poderia comprar de cada moeda estrangeira.

# Considere a tabela de conversão abaixo:
# Dólar Americano:R$4,91 
#Peso Argentino:R$0,02 
#Dólar Australiano:R$3,18
#Dólar Canadense:R$3,64
#Franco Suiço:R$0,42
#Euro:R$5,36
#Libra esterlina:R$6,21

valor = float(input('Quanto dinheiro você tem?: '))

conversao ={
    "Dólar Americano" : 4.91,
    "Peso Argentino" : 0.02,
    "Dólar Australiano" : 3.18,
    "Dólar Canadense" : 3.64,
    "Franco Suiço" : 0.42,
    "Euro" : 5.36,
    "Libra Esterlina" : 6.21,
}

for conversao, valor_conversao in conversao.items():
    print(f'{conversao}: {float(valor)/valor_conversao:.2f}')

#2: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade 
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$80,00 por dia e 
# R$0,20 por km rodado

km = float(input('Digite quantos km foi percorrido: '))
dias = int(input('Digite a quantidade de dias em que o carro foi alugado: '))

total_dias = dias*80
total_km = km*0.20

soma = total_dias+total_km

print(f'O total a pagar é R${soma:.2f}')

#3: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário.
# Se o salário for até R$1000,00 o funcionário terá 20% de aumento.
# Entre R$1001,00 até R$2800,00 o funcionário terá 10% de aumento.
# Acima de R$2801,00 o funcionário terá 5% de aumento.


salario = float(input("Digite seu salário atual: "))

if salario <= 1000:
    calculo = salario*1.2
    print(f'Seu novo salário será: R${calculo:.2f}')

elif salario <= 2800:
    calculo = salario*1.1
    print(f'Seu novo salário será: R${calculo:.2f}')

else:
    calculo = salario*1.05
    print(f'Seu novo salário será: R${calculo:.2f} ')


#4: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor númerico.
# Ex:
# n=leiaInt(‘Digiteumn’)

def leiaInt():
    while True:
      try: 
          return int(input('Digite um número: '))
      except ValueError:
          print('Valor Inválido')

numero = leiaInt()
print(f'O número digitado foi:{numero}')
      

