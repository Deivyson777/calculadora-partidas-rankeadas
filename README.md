# ⚔️ Calculadora de Partidas Rankeadas

Projeto desenvolvido para o **Desafio 2 da DIO (Digital Innovation One)**, com o objetivo de praticar **variáveis, operadores, laços de repetição, estruturas de decisão e funções** utilizando Python.

## 🎯 Objetivo

Criar uma função que receba a quantidade de vitórias e derrotas de um jogador, calcule o **saldo de vitórias** (`vitórias - derrotas`) e retorne seu **nível**, determinado pelo número **total de vitórias**.

| Total de vitórias | Nível |
| --- | --- |
| 0 a 10 | Ferro |
| 11 a 20 | Bronze |
| 21 a 50 | Prata |
| 51 a 80 | Ouro |
| 81 a 90 | Diamante |
| 91 a 100 | Lendário |
| 101 ou mais | Imortal |

> **Nota sobre o enunciado:** a faixa para exatamente 10 vitórias não é definida (o texto usa “menor que 10” e depois “11 a 20”). Para evitar uma lacuna, este projeto considera 10 vitórias como **Ferro**.

## 🗂️ Estrutura

```text
calculadora-partidas-rankeadas/
├── main.py
├── README.md
├── .gitignore
└── tests/
    └── test_main.py
```

## ▶️ Como executar

Requer Python 3.9 ou superior. No terminal, na raiz do projeto:

```bash
python main.py
```

No Windows, também pode utilizar `py main.py`.

**Exemplo de uso:**

```text
=== Calculadora de Partidas Rankeadas ===
Digite a quantidade de vitórias: 75
Digite a quantidade de derrotas: 25
O Herói tem de saldo de 50 está no nível de Ouro
```

## ✅ Como testar

```bash
python -m unittest discover -s tests -v
```

Não são necessárias bibliotecas externas.

## 🧠 Conceitos utilizados

- Variáveis: armazenar entradas e resultados.
- Operadores: subtração e comparações.
- Estruturas de decisão: `if`, `elif`, `else`.
- Funções: `calcular_ranked` e `main`.
- Laços de repetição: `for` nos testes automatizados para validar os níveis.

## 📝 Saída solicitada

`O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**`

O programa apresenta a mesma mensagem sem os asteriscos de destaque Markdown.

## 📄 Licença

Projeto educacional desenvolvido para prática de lógica de programação.
