
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]


def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)


def verificar_vitoria(jogador):
    for i in range(3):

        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False


jogador = "X"
for rodada in range(9):
    mostrar_tabuleiro()
    print(f"Jogador {jogador}, sua vez!")

    linha = int(input("Linha (0, 1, 2): "))
    coluna = int(input("Coluna (0, 1, 2): "))


    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
    else:
        print("Posição ocupada! Tente de novo.")
        continue


    if verificar_vitoria(jogador):
        mostrar_tabuleiro()
        print(f"Jogador {jogador} venceu!")
        break


    jogador = "O" if jogador == "X" else "X"
else:
    mostrar_tabuleiro()
    print("Velha!")