#1: Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0

notas = []
medias = []

quantidadeAlunos = 10
quantidadeNotas = 4

for aluno in range(quantidadeAlunos):
    notas.append([])
    for nota in range(quantidadeNotas):
        notas[aluno].append(
            float(
                input(f'Digite a do {nota+1} do aluno {aluno+1}: ')
            )
        )

for notas in notas:
    medias.append(
        sum(notas) / len(notas)
    )

alunos_aprovados = sum(1 for media in medias if media >= 7.0)

print(f'Alunos com a média maior que 7.0: {alunos_aprovados}')

#2: Faça um programa que permita ao usuário digitar o seu nome e
# em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = input('Digite seu nome: ').upper()
invNome = nome [::-1]

print('{}'.format(invNome))

#3: Escreva um programa em Python onde todos os valores em um dicionário são emitidos.
# Se sim, imprima True. Caso contrário, imprima Falso.

dicionario = {"Caminhote": 'automóvel', "Celular": 'eletrônico', "Cadeira": 'objeto'}
print(dicionario)

valores_emitidos = all(valor for valor in dicionario.values())

if valores_emitidos:
    print('True')

else:
    print('False')


#4: Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.

# As perguntas são:
#"Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

positivo = 0

resposta = input('Telefonou para a vítima? (sim ou não): ')

if resposta.upper() == 'SIM':
    positivo += 1

resposta = input('Esteve no local do crime? (sim ou não): ')

if resposta.upper() == 'SIM':
    positivo += 1

resposta = input('Mora perto da vítima? (sim ou não): ')

if resposta.upper() == 'SIM':
    positivo += 1

resposta = input('Devia para a vítima? (Sim ou não): ')

if resposta.upper() == 'SIM':
    positivo += 1

resposta = input('Já trabalhou para a vítima? (sim ou não): ')

if resposta.upper() == 'SIM':
    positivo += 1

if positivo < 2:
    print('Inocente')

elif positivo >= 2:
    print('Suspeita')

elif positivo < 5:
    print('Cúmplice')

else: 
    print('Assassino') 
