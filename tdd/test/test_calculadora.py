""" Módulo de Teste: calculadora.py """

# Red Green Refactor
# Red: erro porque não existe o codigo ainda.
#   quando primeiros escrevemos o teste, já sabemos como deve ser o método
# Green: o código mínimo que vai passar pelos testes.
# Refactor

import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(-1, -1), -2)
        self.assertEqual(soma(0, 0), 0)
        self.assertEqual(soma(4, 3), 7)
    
    def test_soma_com_zero(self): # Nomes dos testes sempre verboso.
        self.assertEqual(soma(0, 5), 5)
        self.assertEqual(soma(7, 0), 7)

    def test_soma_com_decimais(self):
        self.assertAlmostEqual(soma(2.3, 3.5), 5.8)

    def test_soma_com_tres_argumentos(self):
        self.assertEqual(soma(1, 2, 3), 6)
        self.assertEqual(soma(0, 0, 0), 0)
        self.assertEqual(soma(-1, -2, -3), -6)
        

if __name__ == "__main__":
    unittest.main()