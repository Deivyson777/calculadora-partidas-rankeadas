"""Testes para a calculadora de partidas rankeadas."""
import unittest
from main import calcular_ranked


class TestCalculadoraRanked(unittest.TestCase):
    def test_niveis_e_limites(self):
        casos = [
            (0, "Ferro"), (9, "Ferro"), (10, "Ferro"),
            (11, "Bronze"), (20, "Bronze"),
            (21, "Prata"), (50, "Prata"),
            (51, "Ouro"), (80, "Ouro"),
            (81, "Diamante"), (90, "Diamante"),
            (91, "Lendário"), (100, "Lendário"),
            (101, "Imortal"),
        ]
        for vitorias, esperado in casos:
            with self.subTest(vitorias=vitorias):
                self.assertEqual(calcular_ranked(vitorias, 0)[1], esperado)

    def test_saldo_vitorias(self):
        self.assertEqual(calcular_ranked(75, 25), (50, "Ouro"))
        self.assertEqual(calcular_ranked(2, 7), (-5, "Ferro"))

    def test_valores_negativos(self):
        with self.assertRaises(ValueError):
            calcular_ranked(-1, 0)

    def test_valores_nao_inteiros(self):
        with self.assertRaises(TypeError):
            calcular_ranked(10.5, 2)


if __name__ == "__main__":
    unittest.main()
