import unittest
from unittest import TestCase
from calc import soma

class TestCalc(TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5),10)

    def test_soma_varias_entradas(self):
        
        # valores tupla = ( x, y, retorno )
        x_y_tupla_values = (
            (10, 10, 20),
            (1.5, 1.5, 3),
            (-5, 5, 0)
        )

        for valores_tupla in x_y_tupla_values:
            with self.subTest(valores_tupla=valores_tupla):
                x, y, retorno = valores_tupla
                self.assertEqual(soma(x,y), retorno)


    def test_soma_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('0', 0)

unittest.main(verbosity=2)