import random

numero = random.randint(1, 100)
chances = 1
while chances <= 5:
    chute = int(input("Digite um chute: "))
    diferenca = numero - chute
    if diferenca == 0:
        print("Você acertou!")
        break
    elif diferenca > 0 and diferenca < 5:
        print("Você errou, o número é maior (está quente)")
    elif diferenca > 0:
        print("Você errou, o número é maior (está frio)")
    elif diferenca < 0 and diferenca > -5:
        print("Você errou, o número é menor (está quente)")
    else:
        print("Você errou, o número é menor (está frio)")
    chances = chances + 1
print("Fim do programa, o número era:", numero)