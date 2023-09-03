# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".

from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self._primeiro_nome = nome.split(' ') [0]
        self.ultimo_nome = nome.split(' ') [-1]
        self._telefone = telefone
        self.__renda_mensal = renda_mensal

    @property
    def nome(self):
        return self._primeiro_nome + " " + self.ultimo_nome
    
    @nome.setter
    def nome(self, novo_primeiro_nome, novo_ultimo_nome):
        if type(novo_primeiro_nome) != str:
            raise TypeError('Tipo da variável deve ser str')
        self._nome = novo_primeiro_nome, novo_ultimo_nome

    @property
    def telefone(self):
        return self.telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        if type(novo_telefone) != str:
            raise TypeError('Tipo de variável deve ser str')
        self._telefone = novo_telefone

    @property
    def renda_mensal(self):
        return self.__renda_mensal
    
    @abstractmethod
    def tem_cheque_especial(self):
        pass

class ClienteMulher(Cliente):
        def __init__ (self, nome, telefone, renda_mensal):
            super().__init__(nome, telefone, renda_mensal)

        def tem_cheque_especial(self):
            return True
        
class ClienteHomem(Cliente):
        def __init__ (self, nome, telefone, renda_mensal):
            super().__init__(nome, telefone, renda_mensal)

        def tem_cheque_especial(self):
            return False
        
class ContaCorrente:
    def __init__(self, titular):
        self.__saldo = 0.0
        self.__operacoes = []
        self.__titulares = []
        self.adicionar_titular(titular)

    def adicionar_titular(self, titular):
        self.__titulares.append(titular)

    def depositar(self, valor: float):
        self.__saldo += valor
        self.__operacoes.append(f'Depósito de R${valor:.2f}')

    def sacar(self, valor: float):
        if len(self.__titulares) == 0:
            raise ValueError('A conta não tem titulares')
       
        titular = self.__titulares[0]
        if titular.tem_cheque_especial() == False:
            if valor <= self.__saldo:
                self.__saldo -= valor
                self.__operacoes.append(f'Saque de R${valor:.2f}')
            else:
                raise ValueError('Saldo Insuficiente')
            
        else:
            if valor <= self.__saldo or (self.__saldo - valor) >= -titular.renda_mensal:
                self.__saldo -= valor
                self.__operacoes.append(f'Saque de R${valor:.2f}')

            else:
                raise ValueError('Saldo Insuficiente')
            
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def operacoes(self):
        return self.__operacoes
    
cliente_mulher = ClienteMulher('Felicia Abrahão', '99873456', 3750.0)
cliente_homem = ClienteHomem('Nicholas Serafim', '997523145', 2001.0)

conta1 = ContaCorrente(cliente_mulher)
conta2 = ContaCorrente(cliente_homem)

print(conta1.saldo)
print(conta2.saldo)
print()

conta1.depositar(1300.0)
conta2.depositar(700.0)
print()

print(conta1.saldo)
print(conta2.saldo)
print()

try:
    conta1.sacar(800)
    conta2.sacar(20.0)
    
except ValueError as e:
    print(f'Erro durante a execução: {e}')

print(conta1.operacoes)
print()
print(conta2.operacoes)

print(f'Saldo atual: R${conta1.saldo}')
print(f'Saldo atual: R${conta2.saldo}')