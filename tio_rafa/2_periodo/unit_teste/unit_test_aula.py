import unittest
import unit_test_module as ut

class TestFatorial(unittest.TestCase):
    # Equivalence Partitioning Method
    # entender quais são as diferentes partes do código equivalentes entre si que devem
    # funcionar no tsete para que seja possível dizer que tudo está funcionando
    # Equivalence Class Partitioning (ECP)
    def test_greather_than_1(self):
        # self.assertEqual(ut.fatorial(2),2)
        # self.assertEqual(ut.fatorial(3),6)
        # self.assertEqual(ut.fatorial(4),24)
        self.assertEqual(ut.fatorial(5),120)

    def test_lesser_than_0(self):
        self.assertEqual(ut.fatorial(-7),1)
    
    # Boundary Value Analysis ou Boundary Value Teste
    # quando temos um limite definido, testamos todos os valores em torno do limite
    def test_equal_to_0(self):
        self.assertEqual(ut.fatorial(0),1)

    def test_equal_to_1(self):
        self.assertEqual(ut.fatorial(1),1)

    # Data Type checking
    def test_input_value_type(self):
        self.assertEqual(ut.fatorial(2.0), 2.0)
        self.assertRaises(TypeError, ut.fatorial, "Oi")
                        



#  executa só se alguém executar o arquivo de teste diretamente
if __name__ == "__main__":
    unittest.main()