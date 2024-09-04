import unittest

class TestTremAutonomo(unittest.TestCase):
    
    def test_movimento_basico(self):
        trem = TremAutonomo()
        self.assertEqual(trem.mover(["DIREITA", "DIREITA"]), 2)
    
    def test_movimento_esquerda(self):
        trem = TremAutonomo()
        self.assertEqual(trem.mover(["ESQUERDA"]), -1)
    
    def test_limite_movimentos_totais(self):
        trem = TremAutonomo()
        self.assertEqual(trem.mover(["DIREITA"] * 51), 50)
    
    def test_limite_movimentos_consecutivos(self):
        trem = TremAutonomo()
        with self.assertRaises(ValueError):
            trem.mover(["DIREITA"] * 21)
    
    def test_comando_invalido(self):
        trem = TremAutonomo()
        with self.assertRaises(ValueError):
            trem.mover(["CIMA"])

if __name__ == "__main__":
    unittest.main()
