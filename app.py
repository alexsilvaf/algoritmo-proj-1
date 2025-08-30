# jogo_da_velha.py
# Autor: Alex, Murilo, Paloma
# Um jogo da velha simples para 2 jogadores no terminal.

def criar_tabuleiro():
    return [" "] * 9

def mostrar_tabuleiro(t):
    print()
    print(f"   {t[0]} | {t[1]} | {t[2]}")
    print("  ---+---+---")
    print(f"   {t[3]} | {t[4]} | {t[5]}")
    print("  ---+---+---")
    print(f"   {t[6]} | {t[7]} | {t[8]}")
    print()

def mostrar_guia_posicoes():
    guia = ["1","2","3","4","5","6","7","8","9"]
    print("Mapa de posições (use os números para jogar):")
    mostrar_tabuleiro(guia)

def ha_vencedor(t, simbolo):
    combinacoes = (
        (0,1,2), (3,4,5), (6,7,8),  # linhas
        (0,3,6), (1,4,7), (2,5,8),  # colunas
        (0,4,8), (2,4,6)            # diagonais
    )
    return any(t[a] == t[b] == t[c] == simbolo for a,b,c in combinacoes)

def tabuleiro_cheio(t):
    return all(casa != " " for casa in t)

def obter_jogada(jogador, t):
    while True:
        pos = input(f"Jogador {jogador} - escolha uma posição (1-9): ").strip()
        if pos.isdigit():
            idx = int(pos) - 1
            if 0 <= idx <= 8:
                if t[idx] == " ":
                    return idx
                else:
                    print("⚠️  Essa casa já está ocupada. Tente outra.")
            else:
                print("⚠️  Número fora do intervalo. Escolha de 1 a 9.")
        else:
            print("⚠️  Entrada inválida. Digite um número de 1 a 9.")

def alternar_jogador(atual):
    return "O" if atual == "X" else "X"

def partida():
    tabuleiro = criar_tabuleiro()
    jogador = "X"

    print("\n=== JOGO DA VELHA ===")
    mostrar_guia_posicoes()

    while True:
        mostrar_tabuleiro(tabuleiro)
        idx = obter_jogada(jogador, tabuleiro)
        tabuleiro[idx] = jogador

        if ha_vencedor(tabuleiro, jogador):
            mostrar_tabuleiro(tabuleiro)
            print(f"🎉 Jogador {jogador} venceu! Parabéns!\n")
            break

        if tabuleiro_cheio(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("🤝 Deu velha! Empate.\n")
            break

        jogador = alternar_jogador(jogador)

def main():
    try:
        while True:
            partida()
            resp = input("Quer jogar novamente? (s/n): ").strip().lower()
            if resp != "s":
                print("Até a próxima!")
                return
    except (KeyboardInterrupt, EOFError):
        print("\nEncerrando. Tchau!")

if __name__ == "__main__":
    main()
