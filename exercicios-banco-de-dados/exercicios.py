#1. Crie uma tabela chamada "alunos" com os seguintes campos: 
#id(inteiro), nome(texto), idade(inteiro) e curso(texto)

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR (100), idade INT, curso VARCHAR (100))')

conexao.commit()
conexao.close

#2. Insira, pelo menos, 5 registros de alunos na tabela que você criou no exercício anterior

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(1, "Bethany", 20, "Engenharia")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(2, "Nicholas", 19, "Gastronomia")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(3, "Delilah", 21, "Engenharia")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(4, "Trevor", 23, "Engenharia")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES(5, "Aaliyah", 18, "Tecnologia")')


conexao.commit()
conexao.close

#3. Escreva consultas SQL para realizar as seguintes tarefas: 

# a)Selecionar todos os registros da tabela "alunos".

dados = cursor.execute('SELECT * FROM alunos')

for alunos in dados:
    print(alunos)

# b)Selecionar o nome e a idade dos alunos com mais de 20anos.

dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')

for alunos in dados:
    print(alunos)

# c)Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

dados = cursor.execute('SELECT nome FROM alunos WHERE curso="Engenharia"')

for alunos in dados:
    print(alunos)

# d)Contar o número total de alunos na tabela

dados = cursor.execute('SELECT COUNT(*) FROM alunos')

for alunos in dados:
    print(alunos)

#5. Crie uma tabela chamada "clientes" com os campos: 
#id(chaveprimária), nome(texto), idade(inteiro) e saldo(float). 
# Insira alguns registros de clientes na tabela

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT)')

cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(1, "Barbara", 34, 15600)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(2, "Taylor", 19, 987)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(3, "Aaron", 23, 7700)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(4, "Aurora", 41, 10070)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(5, "Charles", 18, 700)')


conexao.commit()
conexao.close

#Escreva consultas SQL para realizar as seguintes tarefas:

#a)Selecione o nome e a idade dos clientes com idade superior a 30 anos.

dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')

for clientes in dados:
    print(clientes)

# b)Calcule o saldo médio dos clientes.

saldo = 3600 + 1987 + 2700 + 5070 + 1000
saldoMedio = saldo/5
print(f'O saldo médio dos clientes é {saldoMedio:.2f}.')

# c)Encontre o cliente com o saldo máximo.

dados = cursor.execute('SELECT nome, MAX(saldo) FROM clientes ')

for clientes in dados:
    print(clientes)

# d)Conte quantos clientes têm saldo acima de 1000.

dados = cursor.execute('SELECT nome, saldo FROM clientes WHERE saldo>1000')

for clientes in dados:
    print(clientes)

#7.Atualização e Remoção com Condições 

# a)Atualize o saldo de um cliente específico.

cursor.execute('UPDATE clientes SET saldo = 2400 WHERE nome="Charles"')

dados = cursor.execute('SELECT * FROM clientes')
for clientes in dados:
    print(clientes)

# b)Remova um cliente pelo seu ID.

cursor.execute('DELETE FROM clientes  WHERE id=2')
dados = cursor.execute('SELECT * FROM clientes')
for clientes in dados:
    print(clientes)


#8.Crie uma segunda tabela chamada "compras" com os campos: 
# id(chaveprimária), cliente_id(chave estrangeira referenciando o id da tabela"clientes"), produto(texto) e valor(real). 
# Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para 
# exibir o nome do cliente, o produto e o valor de cada compra.

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE compras (id INT, clientes_id INT, produto VARCHAR, valor REAL)')

cursor.execute('INSERT INTO compras(id, clientes_id, produto, valor) VALUES(1, 1, "televisão", 3500)')
cursor.execute('INSERT INTO compras(id, clientes_id, produto, valor) VALUES(3, 3, "óculos", 670)')
cursor.execute('INSERT INTO compras(id, clientes_id, produto, valor) VALUES(4, 4, "celular", 5400)')
cursor.execute('INSERT INTO compras(id, clientes_id, produto, valor) VALUES(5, 5, "kindle", 860)')

dados = cursor.execute('SELECT nome, produto, valor FROM compras INNER JOIN clientes ON compras.clientes_id = clientes.id') 

for compras in dados:
    print(compras)

conexao.commit()
conexao.close
