"""Desafio DIO #2: Calculadora de Partidas Rankeadas."""


def calcular_ranked(vitorias: int, derrotas: int) -> tuple[int, str]:
    """Retorna saldo de vitórias e nível a partir das vitórias totais."""
    if not isinstance(vitorias, int) or isinstance(vitorias, bool) or not isinstance(derrotas, int) or isinstance(derrotas, bool):
        raise TypeError("Vitórias e derrotas precisam ser números inteiros.")
    if vitorias < 0 or derrotas < 0:
        raise ValueError("Vitórias e derrotas não podem ser negativas.")

    saldo = vitorias - derrotas
    if vitorias <= 10:
        nivel = "Ferro"
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nivel = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    return saldo, nivel


def main() -> None:
    print("=== Calculadora de Partidas Rankeadas ===")
    try:
        vitorias = int(input("Digite a quantidade de vitórias: "))
        derrotas = int(input("Digite a quantidade de derrotas: "))
        saldo_vitorias, nivel = calcular_ranked(vitorias, derrotas)
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        return

    print(f"O Herói tem de saldo de {saldo_vitorias} está no nível de {nivel}")


if __name__ == "__main__":
    main()
