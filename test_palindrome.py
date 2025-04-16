from implementacion.palindrome import is_palindrome


import unittest
from src.palindrome import is_palindrome

class TestPalindromeCustom(unittest.TestCase):

    # Pruebas con palabras simples
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("deified"))
        self.assertTrue(is_palindrome("rotor"))
        self.assertTrue(is_palindrome("civic"))

    # Pruebas con frases (ignorando espacios y puntuaciones)
    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("Step on no pets"))
        self.assertTrue(is_palindrome("Evil is a name of a foeman, as I live"))
        self.assertTrue(is_palindrome("Madam in Eden I'm Adam"))

    # Pruebas negativas: no son palíndromos
    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("example"))
        self.assertFalse(is_palindrome("development"))
        self.assertFalse(is_palindrome("This won't work"))

    # Casos límite
    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))  # Cadena vacía
        self.assertTrue(is_palindrome("b"))  # Un solo carácter
        self.assertTrue(is_palindrome("B"))  # Un carácter en mayúscula

if __name__ == '__main__':
    unittest.main()
