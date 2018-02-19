import statistics
import random

quantidade = int(input("Digite a quantidade:"))
numeros_aletorios = []
for i in range(quantidade):
    numero = random.randint(1, 6)
    numeros_aletorios.append(numero)
    print("Número gerado:", numero)
print("Soma:", sum(numeros_aletorios))
print("Máximo:", max(numeros_aletorios))
print("Mínimo:", min(numeros_aletorios))
print("Média:", statistics.mean(numeros_aletorios))
print("Desvio padrão:", statistics.stdev(numeros_aletorios))
