# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro:
    def __init__(self, cor, modelo): 
        self.cor = cor
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0
        self.velocidade_max = 190
        self.velocidade_min = 0
 
    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
        self.velocidade = 0

    def acelerar(self):
        if self.ligado == False:
            return
        
        if self.velocidade < self.velocidade_max:
            self.velocidade += 10

    def desacelerar(self):
        if self.ligado == False:
            return
        
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10
            


    def __str__(self):
        carro.ligado = 'ligado' if self.ligado else 'desligado'
        return f'O carro {self.modelo} da cor {self.cor} está {carro.ligado}, à {self.velocidade} km/h'

# Crie uma instância da classe carro.
carro = Carro('vermelho', 'Chery Omoda')
print(carro)

# Faça o carro "andar" utilizando os métodos da sua classe.
carro.ligar()
print(carro)


for _ in range(7):
    carro.acelerar()

print(carro)

# Faça o carro "parar" utilizando os métodos da sua classe.
carro.desligar()
print(carro)






