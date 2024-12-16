import random

def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    if jogador not in opcoes:
        print("Escolha inválida! Tente novamente.")
        return

    print(f"Você escolheu: {jogador}")
    print(f"O computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        print("Você venceu!")
    else:
        print("Você perdeu!")

# Iniciar o jogo
pedra_papel_tesoura()
