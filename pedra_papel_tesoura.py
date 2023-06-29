import random

# Pontos dos Jogadores
pontos_usuario = 0
pontos_comp = 0

opções = ["r","t", "p"]

while True:
    usuario_choice = input("Escolha: R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair:").lower()

    comp_choice = random.randint(0,2)
    comp_opção = opções[comp_choice]

    if usuario_choice == "q":
        break

    print("O Computador escolheu: " + comp_opção)

    if usuario_choice == comp_opção:
        print("Empate!")

    elif usuario_choice =="r" and comp_opção == "t":
        print("Você Ganhou!")
        pontos_usuario += 1

    elif usuario_choice =="p" and comp_opção == "r":
        print("Você Ganhou!")
        pontos_usuario += 1

    elif usuario_choice =="t" and comp_opção == "p":
        print("Você Ganhou!")
        pontos_usuario += 1

    else:
        print("Você Perdeu!")
        pontos_comp += 1

print("Sua Pontuação foi de:", pontos_usuario)
print("A Pontuação do Computador foi de:", pontos_comp)

if pontos_usuario > pontos_comp:
    print("VITÓRIA!!!")

if pontos_comp > pontos_usuario:
    print("DERROTA!!!")

else:
    print("EMPATE!!!")


print("Até Mais!")