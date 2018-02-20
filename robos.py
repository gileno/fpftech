import random

class Ponto(object):
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '<%s, %s>' % (self.x, self.y)

class Robo(Ponto):
    
    def subir(self):
        if self.x <= 0:
            print('Movimento proibido')
        else:
            self.x = self.x - 1
    def descer(self):
        if self.x >= 9:
            print('Movimento proibido')
        else:
            self.x = self.x + 1
    def esquerda(self):
        if self.y <= 0:
            print('Movimento proibido')
        else:
            self.y = self.y - 1
    def direita(self):
        if self.y >= 9:
            print('Movimento proibido')
        else:
            self.y = self.y + 1

class Recompensa(Ponto):
    
    def __init__(self, nome, x=0, y=0):
        super(Recompensa, self).__init__(x, y)
        self.nome = nome
    
    def __str__(self):
        return '%s <%s, %s>' % (self.nome, self.x, self.y)


recompensas = []
nomes = ['moeda', 'gasolina', 'arma']
for i in range(10):
    r = Recompensa(random.choice(nomes), random.randint(0, 9), random.randint(0, 9))
    recompensas.append(r)
    print(r)

robo1 = Robo(random.randint(0, 9), random.randint(0, 9))

def checar_recompensa(robo, recompensas):
    """
    Imprime o nome da recompensa caso tenha encontrado
    """
    pass

while True:
    movimento = input("Onde deseja ir? digite 'sair' para terminar")
    if movimento == 'subir':
        robo1.subir()
    elif movimento == 'descer':
        robo1.descer()
    elif movimento == 'esquerda':
        robo1.esquerda()
    elif movimento == 'direita':
        robo1.direita()
    elif movimento == 'sair':
        break
    else:
        print('Digite um movimento válido')
    checar_recompensa(robo1, recompensas)
print(robo1)
print('Fim do programa')