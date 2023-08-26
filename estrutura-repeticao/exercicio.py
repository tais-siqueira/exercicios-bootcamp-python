#1: Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1>numero2:
    print(numero1)

else:
    print(numero2)

#2: Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. 
# Imprima a mensagem "BomDia!","BoaTarde!"ou"BoaNoite!"ou"ValorInválido!", conforme o caso

turno = input('Digite em que turno estuda: M - Matutino, V - Vespertino, N - Noturno: ')

if turno.upper() == 'M':
   print('Bom dia!')

elif turno.upper() == 'V':
   print('Boa Tarde!')

elif turno.upper() == 'N':
   print('Boa Noite!')

else: 
   print('Valor Inválido')

#3: Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido

nota = float(input('Digite uma nota entre 0 e 10: '))

while nota<0:
    print('Valor inválido.')
    nota = float(input('Digite uma nota entre 0 e 10: '))

print('Valor Válido')
